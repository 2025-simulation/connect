from typing import Optional
from pydantic import BaseModel, Field

import os
import requests
import asyncio

class Action:
    class Valves(BaseModel):
        INBOX_DIR: str = Field(
            default=os.environ.get("BVTK_INBOX_DIR", os.path.expanduser("~/Developments/simulation/final/connect/bvtk-bridge/inbox")),
            description="Directory to save detected Blender JSON actions",
        )

    def __init__(self):
        self.valves = self.Valves()
        pass

    async def action(
            self,
            body: dict,
            __user__=None,
            __event_emitter__=None,
            __event_call__=None, 
    ) -> Optional[dict]:
        print(f"action:{__name__}")

        response = await __event_call__(
            {
                "type": "input",
                "data": {
                    "title": "write a message",
                    "message": "here write a message to append",
                    "placeholder": "enter your message",
                },
            }
        )
        print(response)

        if __event_emitter__:
            await __event_emitter__(
                {
                    "type": "status",
                    "data": {
                        "description": "adding message",
                        "done": False
                    },
                }
            )
            await asyncio.sleep(1)
            await __event_emitter__({
                "type": "message",
                "data": {"content": response}
            })
