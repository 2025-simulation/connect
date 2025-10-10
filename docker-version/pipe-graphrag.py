"""
title: Pipe GraphRAG
authors: Kauzre Zheng
version: 2.0.0
license: MIT
"""


import subprocess
from pydantic import BaseModel, Field
import os
import time
import threading
import queue


class Pipe:
    class Valves(BaseModel):
        GRAPHRAG_PATH: str = Field(
            default="/app/graphrag/.venv/bin/python",
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
            default=os.path.expanduser("/app/graphrag"),
            description="Working directory for graphrag CLI",
        )
        # JSON detection & save options
        INBOX_DIR: str = Field(
            default=os.environ.get("BVTK_INBOX_DIR", os.path.expanduser("/app/graphrag/inbox")),
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
            {"id": "graphrag_basic_realtime", "name": "GraphRAG Basic Search (Real-time)"},
            {"id": "graphrag_local_realtime", "name": "GraphRAG Local Search (Real-time)"},
            {"id": "graphrag_global_realtime", "name": "GraphRAG Global Search (Real-time)"},
        ]
    
    def pipe(self, body: dict):
        messages = body.get("messages", [])
        if not messages:
            return {"answer": "No message provided"}

        question = messages[-1].get("content", "")
        if not question:
            return {"answer": "Empty question"}

        model_id = body.get("model", "graphrag_basic_realtime")
        method = "basic"
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


    def _advanced_stream_response(self, cmd):
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
                        if output == '' or process.poll() is not None:
                            break
                        if output:
                            output_queue.put(output)
                            
                    stderr_output = process.stderr.read()
                    if stderr_output:
                        output_queue.put(f"[ERROR]{stderr_output}")
                    output_queue.put(None)
                except Exception as e:
                    output_queue.put(f"[ERROR] {str(e)}")
                    output_queue.put(None)

                read_thread = threading.Thread(target=read_output)
                read_thread.daemon = True
                read_thread.start()

                buffer = ""
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

                        while len(buffer) >= self.valves.STREAM_CHUNK_SIZE:
                            chunk = buffer[:self.valves.STREAM_CHUNK_SIZE]
                            buffer = buffer[self.valves.STREAM_CHUNK_SIZE:]

                            yield {
                                "choice": [{
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
                        "content": f"ERROR: {str(e)}"
                    },
                    "finish_reason": "stop"
                }]
            }

    def get_pipe_info(self):
        return {
            "name": "GraphRAG Advanced Streaming Integration",
            "description": "Advanced streaming integration with character-level real-time output",
            "version": "2.0.0",
            "methods": ["basic", "local", "global"],
            "features": ["streaming", "real-time", "character-level", "local-deployment", "typing-effect"]            
        }
