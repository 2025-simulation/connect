from pydantic import BaseModel, Field

class Pipe:
    class Valves(BaseModel):
        MODEL_ID: str = Field(default="")

    def __init__(self):
        self.valves = self.Valves()

    def pipe(self, body: dict):
        # Logic goes here
        print(
            self.valves, body
        )  # This will print the configuration options and the input body
        return "Hello, World!"

