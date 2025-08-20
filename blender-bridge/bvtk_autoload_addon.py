bl_info = {
    "name": "BVTKNodes JSON Autoload",
    "author": "connect",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "Node Editor",
    "description": "Auto-import BVTKNodes JSON files from an inbox directory",
    "category": "System",
}

import bpy
import os
import json
import shutil
import traceback
from bpy.app.handlers import persistent


PROJECT_ROOT = os.environ.get("CONNECT_PROJECT_ROOT", os.path.expanduser("~/Developments/simulation/connect"))


def _resolve_paths():
    pr = os.environ.get("CONNECT_PROJECT_ROOT", PROJECT_ROOT)
    inbox = os.path.join(pr, "bvtk-bridge", "inbox")
    processed = os.path.join(pr, "bvtk-bridge", "processed")
    failed = os.path.join(pr, "bvtk-bridge", "failed")
    cfg_path = os.path.join(pr, "bvtk-bridge", "config.json")
    try:
        if os.path.exists(cfg_path):
            with open(cfg_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
            pr = cfg.get("project_root", pr)
            inbox = cfg.get("inbox_dir", inbox)
            processed = cfg.get("processed_dir", processed)
            failed = cfg.get("failed_dir", failed)
    except Exception:
        pass
    inbox = os.environ.get("BVTK_INBOX_DIR", inbox)
    return pr, inbox, processed, failed


PROJECT_ROOT, INBOX, PROCESSED, FAILED = _resolve_paths()


def ensure_dirs():
    for d in (INBOX, PROCESSED, FAILED):
        os.makedirs(d, exist_ok=True)


ALLOWED_MODIFIERS = {"SUBSURF", "DISPLACE"}
ALLOWED_PRIMITIVES = {"CUBE", "PLANE", "UV_SPHERE"}


def _get_view3d_override():
    win = bpy.context.window
    if not win:
        return None
    for area in win.screen.areas:
        if area.type == 'VIEW_3D':
            region = next((r for r in area.regions if r.type == 'WINDOW'), None)
            if region:
                return {"window": win, "area": area, "region": region}
    return None


def _import_bvtk_json(path: str) -> None:
    # Require a Node Editor area to be available
    win = bpy.context.window
    if not win:
        raise RuntimeError("No active window context available")
    area = None
    region = None
    for a in win.screen.areas:
        if a.type == 'NODE_EDITOR':
            area = a
            region = next((r for r in a.regions if r.type == 'WINDOW'), None)
            break
    if area is None or region is None:
        raise RuntimeError("No NODE_EDITOR area found. Open a Node Editor and try again.")

    with bpy.context.temp_override(window=win, area=area, region=region):
        bpy.ops.node.bvtk_node_tree_import(filepath=path, confirm=True)


def _execute_action(action: dict) -> None:
    t = action.get("type")
    if t == "create_object":
        primitive = action.get("primitive")
        name = action.get("name")
        if primitive not in ALLOWED_PRIMITIVES:
            return
        override = _get_view3d_override()
        if primitive == "CUBE":
            if override:
                with bpy.context.temp_override(**override):
                    bpy.ops.mesh.primitive_cube_add()
            else:
                bpy.ops.mesh.primitive_cube_add()
        elif primitive == "PLANE":
            if override:
                with bpy.context.temp_override(**override):
                    bpy.ops.mesh.primitive_plane_add()
            else:
                bpy.ops.mesh.primitive_plane_add()
        elif primitive == "UV_SPHERE":
            if override:
                with bpy.context.temp_override(**override):
                    bpy.ops.mesh.primitive_uv_sphere_add()
            else:
                bpy.ops.mesh.primitive_uv_sphere_add()
        obj = bpy.context.active_object
        if not obj:
            return
        if name:
            obj.name = name
        loc = action.get("location")
        rot = action.get("rotation")
        scale = action.get("scale")
        if isinstance(loc, list) and len(loc) == 3:
            obj.location = loc
        if isinstance(rot, list) and len(rot) == 3:
            obj.rotation_euler = rot
        if isinstance(scale, list) and len(scale) == 3:
            obj.scale = scale
    elif t == "add_modifier":
        obj_name = action.get("object")
        mod_type = action.get("modifier")
        if mod_type not in ALLOWED_MODIFIERS:
            return
        obj = bpy.data.objects.get(obj_name)
        if not obj:
            return
        mod = obj.modifiers.new(name=mod_type, type=mod_type)
        if mod_type == "SUBSURF":
            levels = int(action.get("levels", 1))
            setattr(mod, "levels", max(0, levels))
        elif mod_type == "DISPLACE":
            strength = float(action.get("strength", 0.1))
            mod.strength = strength
            tex_name = action.get("texture")
            if tex_name:
                tex = bpy.data.textures.get(tex_name)
                if tex is None:
                    tex = bpy.data.textures.new(tex_name, type='NONE')
                mod.texture = tex
    elif t == "set_shade_smooth":
        obj_name = action.get("object")
        obj = bpy.data.objects.get(obj_name)
        if obj and obj.type == 'MESH':
            override = _get_view3d_override()
            if override:
                with bpy.context.temp_override(**override, object=obj):
                    bpy.ops.object.shade_smooth()
            else:
                bpy.ops.object.shade_smooth()


def _execute_plan_dict(plan: dict) -> None:
    actions = plan.get("actions", [])
    for act in actions:
        if isinstance(act, dict):
            _execute_action(act)


def scan_once() -> float:
    ensure_dirs()
    try:
        for name in list(os.listdir(INBOX)):
            if not name.lower().endswith(".json"):
                continue
            src = os.path.join(INBOX, name)
            try:
                # Determine JSON type: BVTK tree vs. action plan
                with open(src, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data, dict) and isinstance(data.get("actions"), list):
                    _execute_plan_dict(data)
                else:
                    _import_bvtk_json(src)
                shutil.move(src, os.path.join(PROCESSED, name))
            except Exception as e:
                traceback.print_exc()
                # Write an error sidecar for quick diagnosis
                try:
                    with open(os.path.join(FAILED, name + ".error.txt"), "w", encoding="utf-8") as ef:
                        ef.write(str(e))
                except Exception:
                    pass
                shutil.move(src, os.path.join(FAILED, name))
    finally:
        return 1.0


@persistent
def register_timer(dummy=None):
    ensure_dirs()
    bpy.app.timers.register(scan_once, persistent=True)


def register():
    register_timer()


def unregister():
    pass


