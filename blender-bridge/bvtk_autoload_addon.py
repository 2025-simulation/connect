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

PROJECT_ROOT = os.environ.get("CONNECT_PROJECT_ROOT", "/home/kazure/Developments/simulation/final")
INBOX_DIR = os.path.join(PROJECT_ROOT, "connect", "bvtk-bridge", "inbox")
PROCESSED_DIR = os.path.join(PROJECT_ROOT, "connect", "bvtk-bridge", "processed")
FAILED_DIR = os.path.join(PROJECT_ROOT, "connect", "bvtk-bridge", "failed")

def ensure_dirs():
    for d in [INBOX_DIR, PROCESSED_DIR, FAILED_DIR]:
        os.makedirs(d, exist_ok=True)

def scan_and_import():
    ensure_dirs()
    try:
        for name in list(os.listdir(INBOX_DIR)):
            if not name.lower().endswith(".json"):
                continue
            src = os.path.join(INBOX_DIR, name)
            try:
                with open(src, "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                # 检测 JSON 类型并处理
                if isinstance(data, dict) and "nodes" in data and "links" in data:
                    # BVtkNodes 节点树
                    print(f"导入 BVtkNodes 节点树: {name}")
                    # 这里可以添加具体的导入逻辑
                elif isinstance(data, dict) and "actions" in data:
                    # Blender 动作计划
                    print(f"执行 Blender 动作计划: {name}")
                    # 这里可以添加具体的动作执行逻辑
                
                # 移动到已处理目录
                shutil.move(src, os.path.join(PROCESSED_DIR, name))
                print(f"文件已处理: {name}")
                
            except Exception as e:
                traceback.print_exc()
                shutil.move(src, os.path.join(FAILED_DIR, name))
                print(f"处理失败: {name} - {e}")
    except Exception as e:
        print(f"扫描目录时发生错误: {e}")

@persistent
def register_timer(dummy=None):
    bpy.app.timers.register(scan_and_import, first_interval=2.0)

def register():
    register_timer()

def unregister():
    pass

if __name__ == "__main__":
    register()
