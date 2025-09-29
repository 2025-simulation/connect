from pydantic import BaseModel, Field

class Pipe:
    class Valves(BaseModel):
        MODEL_ID: str = Field(default="")

    def __init__(self):
        self.valves = self.Valves()

    def pipes(self):
        return [
            {"id": "model_id_1", "name": "model_1"},
        ]

    def pipe(self, body: dict):
        print(self.valves, body)
        model = body.get("model", "")
        return f"{model}: Hello, world!"
