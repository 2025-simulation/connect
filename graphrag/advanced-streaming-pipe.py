import subprocess
from pydantic import BaseModel, Field
import os
import json
import time
import threading
import queue

class Pipe:
    class Valves(BaseModel):
        GRAPHRAG_PATH: str = Field(
            default="~/Developments/simulation/graphrag/.venv/bin/python",
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
        # 获取用户问题
        messages = body.get("messages", [])
        if not messages:
            return {"answer": "No message provided"}
        
        question = messages[-1].get("content", "")
        if not question:
            return {"answer": "Empty question"}
        
        # 根据模型ID选择搜索方法
        model_id = body.get("model", "graphrag-basic-realtime")
        method = "basic"  # 默认方法
        
        if "local" in model_id:
            method = "local"
        elif "global" in model_id:
            method = "global"
        
        # 构建命令
        cmd = [
            os.path.expanduser(self.valves.GRAPHRAG_PATH),
            "-m", "graphrag", "query",
            "--root", self.valves.RAG_ROOT,
            "--method", method,
            "--query", question
        ]
        
        # 检查是否需要流式输出
        is_streaming = body.get("stream", False)
        
        if is_streaming:
            # 返回高级流式响应
            return self._advanced_stream_response(cmd)
        else:
            # 返回普通响应
            return self._get_response(cmd)
    
    def _advanced_stream_response(self, cmd):
        """高级流式输出，支持字符级别的实时显示"""
        try:
            # 启动进程
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True,
                cwd=os.path.expanduser("~/Developments/simulation/graphrag")
            )
            
            # 创建输出队列
            output_queue = queue.Queue()
            
            # 启动输出读取线程
            def read_output():
                try:
                    while True:
                        output = process.stdout.readline()
                        if output == '' and process.poll() is not None:
                            break
                        if output:
                            output_queue.put(output)
                    # 读取错误输出
                    stderr_output = process.stderr.read()
                    if stderr_output:
                        output_queue.put(f"[Error] {stderr_output}")
                    output_queue.put(None)  # 结束信号
                except Exception as e:
                    output_queue.put(f"[Error] {str(e)}")
                    output_queue.put(None)
            
            # 启动读取线程
            read_thread = threading.Thread(target=read_output)
            read_thread.daemon = True
            read_thread.start()
            
            # 流式输出
            buffer = ""
            while True:
                try:
                    # 非阻塞获取输出
                    try:
                        output = output_queue.get(timeout=0.1)
                    except queue.Empty:
                        # 检查进程是否还在运行
                        if process.poll() is not None:
                            break
                        continue
                    
                    if output is None:  # 结束信号
                        break
                    
                    buffer += output
                    
                    # 按字符流式输出
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
                        
                        # 添加延迟以模拟打字效果
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
            
            # 输出剩余缓冲区内容
            if buffer:
                yield {
                    "choices": [{
                        "delta": {
                            "content": buffer
                        },
                        "finish_reason": None
                    }]
                }
            
            # 发送完成信号
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
    
    def _get_response(self, cmd):
        """获取完整响应"""
        try:
            # 执行命令
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=os.path.expanduser("~/Developments/simulation/graphrag")
            )
            
            # 获取输出
            stdout, stderr = process.communicate()
            
            if process.returncode == 0:
                answer = stdout.strip()
                if not answer:
                    answer = "No response generated from GraphRAG"
            else:
                answer = f"Error executing GraphRAG: {stderr.strip()}"
                
        except Exception as e:
            answer = f"Error: {str(e)}"
        
        return {"answer": answer}

    def get_pipe_info(self):
        """返回管道信息"""
        return {
            "name": "GraphRAG Advanced Streaming Integration",
            "description": "Advanced streaming integration with character-level real-time output",
            "version": "2.0.0",
            "methods": ["basic", "local", "global"],
            "features": ["streaming", "real-time", "character-level", "local-deployment", "typing-effect"]
        }
