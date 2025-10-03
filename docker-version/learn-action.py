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

    
class Action:
    class Valves(BaseModel):
        INBOX: str = Field(
            # default = os.path.expanduser("~/Developments/simulation/final/connect/bvtk-bridge/inbox/"),
            defalut = "/app/connect/bvtk-bridge/inbox"
            description = "Directory to save detected Blender JSON actions",
        )

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
                
