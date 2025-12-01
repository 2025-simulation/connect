import subprocess
from pydantic import BaseModel, Field
import os
import time
import threading
import queue

# Try to import JSON helpers for Blender actions; provide robust fallbacks
def _import_schema_utils():
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
                    raise ValueError("JSON must contain an 'actions' list")
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


try_extract_json_from_text, parse_actions_json, save_validated_actions = _import_schema_utils()


def _extract_valid_actions_json(text: str):
    """从文本中尽可能稳健地提取一个符合 actions 架构的 JSON 字符串。

    策略：
    1) 遍历所有三反引号代码块（``` 或 ```json），逐一校验。
    2) 若无代码块匹配，基于出现的 "\"actions\"" 键定位附近的 JSON 子串并尝试解析。
    返回首个通过 parse_actions_json 的 JSON 字符串；否则返回 None。
    """
    try:
        # 1) 扫描代码块
        i = 0
        while True:
            start = text.find("```", i)
            if start == -1:
                break
            # 跳过语言标记
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
                # 仅当 block 可能是 JSON 时尝试
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
        key_pos = text.find('"actions"')
        if key_pos != -1:
            # 向左找到最近的 '{'，向右找到匹配的 '}'（有限深度扫描）
            left = text.rfind('{', 0, key_pos)
            if left != -1:
                # 简单深度计数匹配
                depth = 0
                for j in range(left, len(text)):
                    ch = text[j]
                    if ch == '{':
                        depth += 1
                    elif ch == '}':
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

class Pipe:
    class Valves(BaseModel):
        GRAPHRAG_PATH: str = Field(
            default="~/Developments/simulation/final/graphrag/.venv/bin/python",
            description="Path to graphrag Python executable"
        )
        RAG_ROOT: str = Field(
            default="./ragtest",
            description="Root directory for RAG data"
        )
        DEFAULT_METHOD: str = Field(
            default="basic",
            description="Default search method (basic, local, global)"
        )
        GRAPHRAG_CWD: str = Field(
            default=os.path.expanduser("~/Developments/simulation/final/graphrag"),
            description="Working directory for graphrag CLI",
        )
        # JSON detection & save options
        INBOX_DIR: str = Field(
            default=os.environ.get("BVTK_INBOX_DIR", os.path.expanduser("~/Developments/simulation/final/connect/bvtk-bridge/inbox")),
            description="Directory to save detected Blender JSON actions",
        )
        FILE_PREFIX: str = Field(default="task", description="Saved JSON filename prefix")
        SAVE_JSON_FROM_OUTPUT: bool = Field(
            default=False,
            description="Detect JSON in graphrag stdout and save to inbox",
        )
        STREAM_CHUNK_SIZE: int = Field(
            default=10,
            description="Number of characters to stream at once"
        )
        STREAM_DELAY: float = Field(
            default=0.05,
            description="Delay between stream chunks in seconds"
        )

    def __init__(self):
        self.valves = self.Valves()

    def pipes(self):
        return [
            {"id": "graphrag-basic-realtime", "name": "GraphRAG Basic Search (Real-time)"},
            {"id": "graphrag-local-realtime", "name": "GraphRAG Local Search (Real-time)"},
            {"id": "graphrag-global-realtime", "name": "GraphRAG Global Search (Real-time)"},
        ]

    def pipe(self, body: dict):
        try:
            
            messages = body.get("messages", [])
            question = messages[-1].get("content", "")
            
            model_id = body.get("model", "graphrag-basic-realtime")
            method = "basic"  # 默认方法
        
            if "local" in model_id:
                method = "local"
            elif "global" in model_id:
                method = "global"
        
            cmd = [
                os.path.expanduser(self.valves.GRAPHRAG_PATH),
                "-m", "graphrag", "query",
                "--root", self.valves.RAG_ROOT,
                "--method", method,
                "--query", question
            ]

            return self._advanced_stream_response(cmd)

        except Exception as e:
            return [
                {
                    "id": "error",
                    "name": f"Error failed to access the question:\n{e}",
                },
            ]            

        
    def _advanced_stream_response(self, cmd):
        """高级流式输出，支持字符级别的实时显示"""
        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True,
                cwd=self.valves.GRAPHRAG_CWD
            )
            
            output_queue = queue.Queue()
            
            def read_output():
                try:
                    while True:
                        output = process.stdout.readline()
                        if output == '' and process.poll() is not None:
                            break
                        if output:
                            output_queue.put(output)
                    stderr_output = process.stderr.read()
                    if stderr_output:
                        output_queue.put(f"[Error] {stderr_output}")
                    output_queue.put(None)  # 结束信号
                except Exception as e:
                    output_queue.put(f"[Error] {str(e)}")
                    output_queue.put(None)
            
            read_thread = threading.Thread(target=read_output)
            read_thread.daemon = True
            read_thread.start()
            
            buffer = ""
            json_saved = False
            while True:
                try:
                    try:
                        output = output_queue.get(timeout=0.1)
                    except queue.Empty:
                        if process.poll() is not None:
                            break
                        continue
                    
                    if output is None:
                        break
                    
                    buffer += output

                    if self.valves.SAVE_JSON_FROM_OUTPUT and not json_saved:
                        try:
                            candidate = _extract_valid_actions_json(buffer) or try_extract_json_from_text(buffer)
                            if candidate:
                                plan = parse_actions_json(candidate)
                                path = save_validated_actions(plan, self.valves.INBOX_DIR, prefix=self.valves.FILE_PREFIX)
                                json_saved = True
                                buffer += f"\n[Saved JSON to: {path}]\n"
                        except Exception:
                            pass
                    
                    while len(buffer) >= self.valves.STREAM_CHUNK_SIZE:
                        chunk = buffer[:self.valves.STREAM_CHUNK_SIZE]
                        buffer = buffer[self.valves.STREAM_CHUNK_SIZE:]
                        
                        yield {
                            "choices": [{
                                "delta": {
                                    "content": chunk
                                },
                                "finish_reason": None
                            }]
                        }
                        
                        time.sleep(self.valves.STREAM_DELAY)
                    
                except Exception as e:
                    yield {
                        "choices": [{
                            "delta": {
                                "content": f"Error: {str(e)}"
                            },
                            "finish_reason": None
                        }]
                    }
                    break
            
            if buffer:
                yield {
                    "choices": [{
                        "delta": {
                            "content": buffer
                        },
                        "finish_reason": None
                    }]
                }
            
            yield {
                "choices": [{
                    "delta": {},
                    "finish_reason": "stop"
                }]
            }
            
        except Exception as e:
            yield {
                "choices": [{
                    "delta": {
                        "content": f"Error: {str(e)}"
                    },
                    "finish_reason": "stop"
                }]
            }
