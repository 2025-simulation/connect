bl_info = {
    "name": "BVTKNodes JSON Autoload test",
    "author": "Kazure Zheng",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "Node Editor",
    "description": "Auto-import BVTKNodes JSON files from an inbox directory",
    "category": "System",
}


import bpy
import os
import shutil
import traceback
from bpy.app.handlers import persistent

# PROJECT_ROOT = os.path.expanduser("/app/connect")
PROJECT_ROOT = "/app/connect"
INBOX = os.path.join(PROJECT_ROOT, "inbox")
PROCESSED = os.path.join(PROJECT_ROOT, "processed")
FAILED = os.path.join(PROJECT_ROOT, "failed")

def ensure_dirs():
    for d in (INBOX, PROCESSED, FAILED):
        os.makedirs(d, exist_ok=True)


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


def scan_once(path: str) -> float:
    ensure_dirs()
    try:
        for name in list(os.listdir(path)):
            src = os.path.join(path, name)
            if not name.lower().endswith(".json"):
                shutil.move(src, os.path.join(FAILED, name))
                continue
            try:
                _import_bvtk_json(src)
                shutil.move(src, os.path.join(PROCESSED, name))
            except Exception:
                traceback.print_exc()
                shutil.move(src, os.path.join(FAILED, name))
    finally:
        return 1.0
    
# @persistent
# def register_timer(dummy=None):
#     ensure_dirs()
#     bpy.app.timers.register(scan_once(INBOX), first_interval=2.0, persistent=True)
# # The corrected registration
@persistent
def register_timer(dummy=None):
    ensure_dirs()

    bpy.app.timers.register(
        lambda: scan_once(INBOX), 
        first_interval=2.0, 
        persistent=True
    )


def register():
    register_timer()

def unregister():
    pass

