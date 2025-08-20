import os
import sys
import subprocess
from pathlib import Path
from typing import Any, Dict

import requests
from pydantic import BaseModel, Field


# Robust import of local package `schemas`
def _import_schema_utils():
    """Import schema helpers with robust fallbacks.

    Returns a tuple: (try_extract_json_from_text, parse_actions_json, save_validated_actions)
    """
    try:
        from schemas.blender_actions import (
            try_extract_json_from_text,
            parse_actions_json,
            save_validated_actions,
        )
        return try_extract_json_from_text, parse_actions_json, save_validated_actions
    except Exception:
        # Try to add project root and re-import
        try:
            project_root = os.environ.get("CONNECT_PROJECT_ROOT") or str(Path(__file__).resolve().parents[1])
            if project_root not in sys.path:
                sys.path.append(project_root)
            from schemas.blender_actions import (  # type: ignore
                try_extract_json_from_text,
                parse_actions_json,
                save_validated_actions,
            )
            return try_extract_json_from_text, parse_actions_json, save_validated_actions
        except Exception:
            # Final fallback: lightweight implementations
            import json

            def _try_extract_json_from_text(text: str):
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

            def _parse_actions_json(json_str: str):
                data = json.loads(json_str)
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
                    content = json.dumps(plan, ensure_ascii=False, indent=2)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                return path

            return _try_extract_json_from_text, _parse_actions_json, _save_validated_actions


try_extract_json_from_text, parse_actions_json, save_validated_actions = _import_schema_utils()


SYSTEM_INSTRUCTIONS = (
    "You are a tool that outputs ONLY JSON for Blender actions. "
    "Follow this schema strictly: {version:int, doc?:str, actions:list}. "
    "Each action must be one of: \n"
    "- create_object: {type:'create_object', object_type:'MESH', primitive:'CUBE|PLANE|UV_SPHERE', name?:str, location?:[x,y,z], rotation?:[rx,ry,rz], scale?:[sx,sy,sz]}\n"
    "- add_modifier: {type:'add_modifier', object:str, modifier:'SUBSURF|DISPLACE', levels?:int, strength?:float, texture?:str}\n"
    "- set_shade_smooth: {type:'set_shade_smooth', object:str}\n"
    "- create_texture: {type:'create_texture', name:str, kind:'NOISE|VORONOI', params?:{}}\n"
    "Also allowed: import_file: {type:'import_file', kind:'OBJ|FBX|GLTF|GLB', path:str, into_collection?:str}.\n"
    "Output ONLY a single JSON object. No explanations."
)


class Pipe:
    class Valves(BaseModel):
        # GraphRAG settings
        GRAPHRAG_PATH: str = Field(default=os.path.expanduser("~/Developments/simulation/graphrag/.venv/bin/python"))
        RAG_ROOT: str = Field(default="./ragtest")
        DEFAULT_METHOD: str = Field(default="basic")
        GRAPHRAG_CWD: str = Field(default=os.path.expanduser("~/Developments/simulation/graphrag"), description="Working directory for graphrag CLI")
        ENABLE_GRAPHRAG: bool = Field(default=True, description="If false, skip graphrag and send empty context to LLM")
        GRAPHRAG_EMITS_JSON: bool = Field(default=True, description="Treat GraphRAG stdout as final Blender JSON and save directly (no LLM)")
        PROMPT_PREFIX: str = Field(
            default=(
                "Return ONLY a single JSON object following this schema: "
                "{version:int, doc?:str, actions:[create_object|add_modifier|set_shade_smooth|create_texture|import_file]}. "
                "No prose, no markdown fences."
            ),
            description="Prefix added before user question to instruct GraphRAG to reply with Blender-actions JSON",
        )
        PROMPT_SUFFIX: str = Field(default="", description="Optional suffix appended to the question")

        # OpenAI-compatible LLM
        OPENAI_API_BASE_URL: str = Field(default="http://localhost:11434/v1", description="OpenAI-compatible base URL, e.g. Ollama/OpenWebUI/LM Studio")
        OPENAI_API_KEY: str = Field(default="", description="API key if required; leave empty if not needed")
        OPENAI_MODEL: str = Field(default="gpt-4o-mini", description="Model name")
        LLM_TIMEOUT_SEC: int = Field(default=30, description="HTTP timeout for LLM request")
        FALLBACK_SAMPLE_ON_ERROR: bool = Field(default=True, description="If LLM fails, write a small sample plan to test the pipeline")

        # Output inbox
        INBOX_DIR: str = Field(default=os.environ.get("BVTK_INBOX_DIR", os.path.expanduser("~/Developments/simulation/connect/bvtk-bridge/inbox")))
        FILE_PREFIX: str = Field(default="task")

    def __init__(self):
        self.valves = self.Valves()

    def pipes(self):
        return [
            {"id": "graphrag-to-bvtk-json", "name": "GraphRAG → BVTK JSON (Auto Save)"},
        ]

    def _run_graphrag(self, question: str, method: str) -> str:
        # Attach prefix/suffix so GraphRAG LLM按我们需求输出JSON
        full_query = f"{self.valves.PROMPT_PREFIX}\n\n{question}"
        if self.valves.PROMPT_SUFFIX:
            full_query = f"{full_query}\n\n{self.valves.PROMPT_SUFFIX}"

        cmd = [
            os.path.expanduser(self.valves.GRAPHRAG_PATH),
            "-m",
            "graphrag",
            "query",
            "--root",
            self.valves.RAG_ROOT,
            "--method",
            method,
            "--query",
            full_query,
        ]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=self.valves.GRAPHRAG_CWD)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            raise RuntimeError(f"GraphRAG failed: {stderr.strip()}")
        return stdout.strip()

    def _llm_to_json(self, prompt: str, context: str) -> str:
        headers = {"Content-Type": "application/json"}
        if self.valves.OPENAI_API_KEY:
            headers["Authorization"] = f"Bearer {self.valves.OPENAI_API_KEY}"
        payload = {
            "model": self.valves.OPENAI_MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_INSTRUCTIONS},
                {"role": "user", "content": f"Request:\n{prompt}\n\nContext:\n{context}"},
            ],
            "temperature": 0,
        }
        r = requests.post(
            f"{self.valves.OPENAI_API_BASE_URL}/chat/completions",
            json=payload,
            headers=headers,
            timeout=self.valves.LLM_TIMEOUT_SEC,
        )
        r.raise_for_status()
        data = r.json()
        content = data["choices"][0]["message"]["content"]
        return content

    def _sample_plan(self) -> dict:
        return {
            "version": 1,
            "doc": "Sample plan generated as fallback",
            "actions": [
                {"type": "create_object", "object_type": "MESH", "primitive": "CUBE", "name": "DemoCube"},
                {"type": "add_modifier", "object": "DemoCube", "modifier": "SUBSURF", "levels": 2},
                {"type": "set_shade_smooth", "object": "DemoCube"},
            ],
        }

    def pipe(self, body: Dict[str, Any]):
        messages = body.get("messages", [])
        if not messages:
            return {"answer": "No message provided"}
        question = messages[-1].get("content", "").strip()
        if not question:
            return {"answer": "Empty message"}

        # choose method by model name suffix
        model_id = body.get("model", "")
        method = self.valves.DEFAULT_METHOD
        if "local" in model_id:
            method = "local"
        elif "global" in model_id:
            method = "global"

        if self.valves.ENABLE_GRAPHRAG:
            try:
                context = self._run_graphrag(question, method)
            except Exception as e:
                # Continue with empty context, but inform user
                context = ""
                print(f"[graphrag-to-bvtk-json] GraphRAG error (continuing without context): {e}")
        else:
            context = ""

        # If GraphRAG 直接输出的是我们需要的 JSON，优先短路保存，完全不需要任何 API
        if self.valves.ENABLE_GRAPHRAG and self.valves.GRAPHRAG_EMITS_JSON and context:
            candidate = try_extract_json_from_text(context) or context
            try:
                plan = parse_actions_json(candidate)
                path = save_validated_actions(plan, self.valves.INBOX_DIR, prefix=self.valves.FILE_PREFIX)
                return {"answer": f"Saved Blender actions (from GraphRAG) to: {path}"}
            except Exception as e:
                # 若解析失败，再走 LLM 或示例兜底
                print(f"[graphrag-to-bvtk-json] Failed to parse GraphRAG JSON, falling back to LLM: {e}")

        if not self.valves.OPENAI_API_BASE_URL:
            if self.valves.FALLBACK_SAMPLE_ON_ERROR:
                path = save_validated_actions(self._sample_plan(), self.valves.INBOX_DIR, prefix=self.valves.FILE_PREFIX)
                return {"answer": f"LLM not configured. Wrote sample plan to: {path}"}
            return {"answer": "LLM endpoint not configured (OPENAI_API_BASE_URL)."}

        try:
            raw = self._llm_to_json(question, context)
        except Exception as e:
            if self.valves.FALLBACK_SAMPLE_ON_ERROR:
                path = save_validated_actions(self._sample_plan(), self.valves.INBOX_DIR, prefix=self.valves.FILE_PREFIX)
                return {"answer": f"LLM error: {e}. Wrote sample plan to: {path}"}
            return {"answer": f"LLM error: {e}"}

        candidate = try_extract_json_from_text(raw) or raw
        try:
            plan = parse_actions_json(candidate)
        except Exception as e:
            return {"answer": f"JSON validation failed: {e}\nRaw: {raw[:500]}"}

        try:
            path = save_validated_actions(plan, self.valves.INBOX_DIR, prefix=self.valves.FILE_PREFIX)
            return {"answer": f"Saved Blender actions to: {path}"}
        except Exception as e:
            return {"answer": f"Failed to save JSON: {e}"}


