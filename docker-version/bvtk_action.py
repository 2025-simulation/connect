from typing import Optional
from pydantic import BaseModel, Field

import os
import requests
import asyncio
import json
import time

# JSON 处理工具函数
def _import_schema_utils():
    """导入 JSON 处理工具，提供回退实现"""
    try:
        from schemas.blender_actions import (
            try_extract_json_from_text,
            parse_actions_json,
            save_validated_actions,
        )
        return try_extract_json_from_text, parse_actions_json, save_validated_actions
    except Exception:
        try:
            # Add project root for relative import when running from OpenWebUI
            from pathlib import Path
            project_root = os.environ.get("CONNECT_PROJECT_ROOT") or str(Path(__file__).resolve().parents[1])
            if project_root not in os.sys.path:
                os.sys.path.append(project_root)
            from schemas.blender_actions import (  # type: ignore
                try_extract_json_from_text,
                parse_actions_json,
                save_validated_actions,
            )
            return try_extract_json_from_text, parse_actions_json, save_validated_actions
        except Exception:
            # Last resort lightweight implementations
            import json as _json

            def _try_extract_json_from_text(text: str):
                fences = ["```json", "```JSON", "```"]
                for fence in fences:
                    if fence in text:
                        try:
                            start = text.index(fence) + len(fence)
                            end = text.index("```", start)
                            candidate = text[start:end].strip()
                            _json.loads(candidate)
                            return candidate
                        except Exception:
                            pass
                try:
                    start = text.index("{")
                    end = text.rindex("}") + 1
                    candidate = text[start:end]
                    _json.loads(candidate)
                    return candidate
                except Exception:
                    return None

            def _parse_actions_json(json_str: str):
                data = _json.loads(json_str)
                if not isinstance(data, dict) or not isinstance(data.get("actions"), list):
                    raise ValueError("JSON must contain an actions list")
                return data

            def _save_validated_actions(plan, inbox_dir: str, prefix: str = "task"):
                from time import strftime
                os.makedirs(inbox_dir, exist_ok=True)
                ts = strftime("%Y%m%d-%H%M%S")
                path = os.path.join(inbox_dir, f"{prefix}-{ts}.json")
                if hasattr(plan, "model_dump_json"):
                    content = plan.model_dump_json(indent=2, by_alias=True)
                else:
                    content = _json.dumps(plan, ensure_ascii=False, indent=2)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                return path

            return _try_extract_json_from_text, _parse_actions_json, _save_validated_actions

# 导入 JSON 处理工具
try_extract_json_from_text, parse_actions_json, save_validated_actions = _import_schema_utils()

def _extract_valid_actions_json(text: str):
    """从 Markdown 格式文本中提取符合 actions 架构的 JSON 字符串"""
    import re
    
    try:
        # 1) 扫描代码块
        i = 0
        while True:
            start = text.find("```", i)
            if start == -1:
                break
            lang_end = text.find("\n", start + 3)
            if lang_end == -1:
                break
            lang = text[start + 3:lang_end].strip().lower()
            end = text.find("```", lang_end)
            if end == -1:
                break
            block = text[lang_end + 1:end]
            candidate = block.strip()
            try:
                if candidate.startswith("{") and candidate.endswith("}"):
                    parse_actions_json(candidate)
                    return candidate
            except Exception:
                pass
            i = end + 3
    except Exception:
        pass

    # 2) 基于 "actions" 键的启发式截取
    try:
        key_pos = text.find("\"actions\"")
        if key_pos != -1:
            left = text.rfind("{", 0, key_pos)
            if left != -1:
                depth = 0
                for j in range(left, len(text)):
                    ch = text[j]
                    if ch == "{":
                        depth += 1
                    elif ch == "}":
                        depth -= 1
                        if depth == 0:
                            candidate = text[left:j + 1]
                            try:
                                parse_actions_json(candidate)
                                return candidate
                            except Exception:
                                break
    except Exception:
        pass

    return None

class Action:
    class Valves(BaseModel):
        INBOX_DIR: str = Field(
            default=os.environ.get("BVTK_INBOX_DIR", os.path.expanduser("~/Developments/simulation/final/connect/bvtk-bridge/inbox")),
            description="Directory to save detected Blender JSON actions",
        )
        FILE_PREFIX: str = Field(default="task", description="Saved JSON filename prefix")

    def __init__(self):
        self.valves = self.Valves()

    async def action(
            self,
            body: dict,
            __user__=None,
            __event_emitter__=None,
            __event_call__=None, 
    ) -> Optional[dict]:
        """
        Action Function 处理当前消息中的 JSON 提取
        
        根据 Open WebUI Action Functions 文档：
        - 不需要用户输入
        - 直接从 body 参数获取消息内容
        - 添加按钮到消息下方
        """
        print(f"action:{__name__}")

        # 从 body 中获取消息内容
        message_content = ""
        if isinstance(body, dict):
            # 尝试从不同可能的字段获取消息内容
            message_content = (
                body.get("content") or 
                body.get("message") or 
                body.get("text") or 
                str(body)
            )
        else:
            message_content = str(body)

        print(f"处理消息内容: {message_content[:100]}...")

        if __event_emitter__:
            await __event_emitter__({
                "type": "status",
                "data": {
                    "description": "正在分析消息中的 JSON...",
                    "done": False
                },
            })

        # 尝试从消息内容中提取 JSON
        try:
            # 首先尝试使用高级提取方法
            candidate = _extract_valid_actions_json(message_content)
            if not candidate:
                # 回退到基础提取方法
                candidate = try_extract_json_from_text(message_content)
            
            if candidate:
                # 解析并保存 JSON
                plan = parse_actions_json(candidate)
                path = save_validated_actions(plan, self.valves.INBOX_DIR, prefix=self.valves.FILE_PREFIX)
                
                result_message = f"✅ **JSON 提取成功！**\n\n📁 **保存路径**: `{path}`\n\n📄 **JSON 内容**:\n```json\n{candidate}\n```"
                
                await __event_emitter__({
                    "type": "message",
                    "data": {"content": result_message}
                })
                
                # 发送完成状态
                await __event_emitter__({
                    "type": "status",
                    "data": {
                        "description": "JSON 提取完成",
                        "done": True
                    },
                })
                
                return {"success": True, "path": path, "json_content": candidate}
            else:
                error_message = "❌ **未找到有效的 JSON 内容**\n\n请确保消息包含以下格式之一:\n- 代码块: ```json\n{...}\n```\n- 包含 actions 键的 JSON 对象"
                
                await __event_emitter__({
                    "type": "message",
                    "data": {"content": error_message}
                })
                
                await __event_emitter__({
                    "type": "status",
                    "data": {
                        "description": "未找到有效 JSON",
                        "done": True
                    },
                })
                
                return {"success": False, "error": "No valid JSON found"}
                
        except Exception as e:
            error_message = f"❌ **处理过程中出现错误**: {str(e)}"
            
            await __event_emitter__({
                "type": "message",
                "data": {"content": error_message}
            })
            
            await __event_emitter__({
                "type": "status",
                "data": {
                    "description": "处理失败",
                    "done": True
                },
            })
            
            return {"success": False, "error": str(e)}
