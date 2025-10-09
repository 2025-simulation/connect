from pydantic import BaseModel, Field
from time import strftime

import os

def extract_text(text, text_begin, text_end):
    begin = text.rfind(text_begin)
    if begin == -1:
        return None
    begin += len(text_begin)
    end = text.find(text_end, begin)
    if end == -1:
        end = len(text)
    return text[begin:end]


class Action:
    class Valves(BaseModel):
        INBOX: str = Field(
            default = "/app/connect/bvtk-bridge/inbox",
            description = "testing"
        )

    def __init__(self):
        self.valves = self.Valves()

    async def action(
            self,
            body: dict,
            __user__=None,
            __event_emitter__=None,
            __event_call__=None,
    ):
        content = body["messages"][-1]["content"]
        try:
            # await __event_emitter__({
            #     "type": "notification",
            #     "data": {"type": "info",
            #              "content": f"Successfully extracted the content"}
            # })

            source = extract_text(content, "```json", "```")
            if source :
                # await __event_emitter__({
                #     "type": "notification",
                #     "data": {"type": "info",
                #              "content": f"{source}"}
                # })
                timestamp = strftime("%Y%m%d-%H%M%S")
                path = os.path.join(self.valves.INBOX, f"{timestamp}.json")
                # path = os.path.join(self.valves.INBOX, "test.json")
                try:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(source)
                    await __event_emitter__({
                        "type": "notification",
                        "data": {"type": "info",
                                 "content": f"Successfully store the JSON in {path}"}
                    })
                except Exception as e:
                    await __event_emitter__({
                        "type": "notification",
                        "data": {"type": "error",
                                 "content": f"Error {str(e)}"}
                    })
            else:
                await __event_emitter__({
                    "type": "notification",
                    "data": {"type": "error",
                             "content": f"Failed to extract code:\n{source}"}
                })
        except Exception as e:
            await __event_emitter__({
                "type": "notification",
                "data": {"type": "error",
                         "content": f"Action failed:\n{str(e)}"}
            })
