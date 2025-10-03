from typing import Optional
from pydantic import BaseModel, Field

import os
import json

def try_extract_json_from_text(text: str):
    fences = ["```json", "```JSON", "```"]
    for fence in fences:
        if fence in text:
            try:
                start = text.index(fence) + len(fence)
                end = text.index("```", start)
                candidate = text[start:end].strip()
                json.loads(candidate)
                return candidate
            except Exception:
                pass
    try:
        start = text.index("{")
        end = text.rindex("}") + 1
        candidate = text[start:end]
        json.loads(candidate)
        return candidate
    except Exception:
        return None

def save_validated_actions(plan, inbox_dir: str, prefix: str = "task"):
    from time import strftime
    os.makedirs(inbox_dir, exist_ok=True)
    ts = strftime("%Y%m%d-%H%M%S")
    path = os.path.join(inbox_dir, f"{prefix}-{ts}.json")
    if hasattr(plan, "model_dump_json"):
        content = plan.model_dump_json(indent=2, by_alias=True)
    else:
        content = json.dumps(plan, ensure_ascii=False, indent=2)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path
class Action:
    class Valves(BaseModel):
        INBOX: str = Field(
            # default = os.path.expanduser("~/Developments/simulation/final/connect/bvtk-bridge/inbox/"),
            defalut = "/app/connect/bvtk-bridge/inbox"
            description = "Directory to save detected Blender JSON actions",
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

        message_content = ""
        if isinstance(body, dict):
            message_content = (
                body.get("content") or
                body.get("message") or
                body.get("text") or
                str(body)
            )

        print(f"processing the message: {message_content[:100]}...")

        if __event_emitter__:
            await __event_emitter__({
                "type": "status",
                "data": {
                    "description": "processing the JSON in message",
                    "done": False
                },
            })

        try:
            candidate = try_extract_json_from_text(message_content)
            if candidate:
                plan = json.loads(candidate)
                path = save_validated_actions(plan, self.valves.INBOX, prefix=self.valves.FILE_PREFIX)

                result_message = f"json 提取成功，\n保存路径是 {path}\n 内容是 {candidate}\n"

                await __event_emitter__({
                    "type": "message",
                    "data": {"content": result_message}
                })

                await __event_emitter__({
                    "type": "status",
                    "data": {
                        "description": "JSON 提取成功"
                        "done": True
                    },
                })

                return {"success": True, "path": path, "json_content": candidate}
            else:
                error_message = "没有找到有效的 JSON 内容"

                await __event_emitter__({
                    "type": "message",
                    "data": {"content": error_message}
                })

                await __event_emitter__({
                    "type": "status",
                    "data": {
                        "description": "未找到有效的 JSON",
                        "done": True
                    },
                })
                return {"success": False, "error": "No valid JSON found"}
        except Exception as e:
            error_message = f"处理过程中出现错误: {str(e)}"

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
