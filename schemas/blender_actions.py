from __future__ import annotations

from typing import List, Literal, Optional, Union, Dict, Any
from pydantic import BaseModel, Field, ValidationError, field_validator
import json
import os
import time


AllowedPrimitive = Literal["CUBE", "PLANE", "UV_SPHERE"]
AllowedModifier = Literal["SUBSURF", "DISPLACE"]
AllowedTextureKind = Literal["NOISE", "VORONOI"]
AllowedImportKind = Literal["OBJ", "FBX", "GLTF", "GLB"]


class CreateObjectAction(BaseModel):
    type: Literal["create_object"]
    object_type: Literal["MESH"] = Field(default="MESH")
    primitive: AllowedPrimitive
    name: Optional[str] = None
    location: Optional[List[float]] = Field(default=None, description="[x, y, z]")
    rotation: Optional[List[float]] = Field(default=None, description="[rx, ry, rz] radians")
    scale: Optional[List[float]] = Field(default=None, description="[sx, sy, sz]")

    @field_validator("location", "rotation", "scale")
    @classmethod
    def _validate_vec3(cls, v: Optional[List[float]]):
        if v is None:
            return v
        if not isinstance(v, list) or len(v) != 3:
            raise ValueError("Must be a list of 3 floats")
        return v


class AddModifierAction(BaseModel):
    type: Literal["add_modifier"]
    object: str
    modifier: AllowedModifier
    levels: Optional[int] = Field(default=None, description="For SUBSURF")
    strength: Optional[float] = Field(default=None, description="For DISPLACE")
    texture: Optional[str] = Field(default=None, description="Texture name for DISPLACE")


class SetShadeSmoothAction(BaseModel):
    type: Literal["set_shade_smooth"]
    object: str


class CreateTextureAction(BaseModel):
    type: Literal["create_texture"]
    name: str
    kind: AllowedTextureKind
    params: Dict[str, Any] = Field(default_factory=dict)


Action = Union[
    CreateObjectAction,
    AddModifierAction,
    SetShadeSmoothAction,
    CreateTextureAction,
]


class ImportFileAction(BaseModel):
    type: Literal["import_file"]
    kind: AllowedImportKind
    path: str = Field(description="Path to the file to import. Relative paths are resolved against the project's assets directory.")
    into_collection: Optional[str] = Field(default=None, description="Optional target collection name")



class BlenderPlan(BaseModel):
    version: int = Field(default=1)
    doc: Optional[str] = None
    actions: List[Union[Action, ImportFileAction]]

    def to_json(self) -> str:
        return self.model_dump_json(indent=2, by_alias=True)


def parse_actions_json(json_str: str) -> BlenderPlan:
    return BlenderPlan.model_validate_json(json_str)


def try_extract_json_from_text(text: str) -> Optional[str]:
    # Try fenced code block first
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

    # Fallback: naive first-brace to last-brace extraction
    try:
        start = text.index("{")
        end = text.rindex("}") + 1
        candidate = text[start:end]
        json.loads(candidate)
        return candidate
    except Exception:
        return None


def save_validated_actions(plan: BlenderPlan, inbox_dir: str, prefix: str = "task") -> str:
    os.makedirs(inbox_dir, exist_ok=True)
    ts = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{prefix}-{ts}.json"
    path = os.path.join(inbox_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(plan.to_json())
    return path


__all__ = [
    "BlenderPlan",
    "CreateObjectAction",
    "AddModifierAction",
    "SetShadeSmoothAction",
    "CreateTextureAction",
    "ImportFileAction",
    "parse_actions_json",
    "try_extract_json_from_text",
    "save_validated_actions",
]


