#!/usr/bin/env python3
"""
Open WebUI Action Functions 设置脚本
自动配置 BVtkNodes JSON 处理环境
"""

import os
import json
import shutil
from pathlib import Path

def setup_directories():
    """设置必要的目录结构"""
    project_root = os.environ.get("CONNECT_PROJECT_ROOT", "/home/kazure/Developments/simulation/final")
    
    directories = [
        os.path.join(project_root, "connect", "bvtk-bridge", "inbox"),
        os.path.join(project_root, "connect", "bvtk-bridge", "processed"),
        os.path.join(project_root, "connect", "bvtk-bridge", "failed"),
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ 创建目录: {directory}")
    
    return directories

def create_config_file():
    """创建配置文件"""
    project_root = os.environ.get("CONNECT_PROJECT_ROOT", "/home/kazure/Developments/simulation/final")
    config_path = os.path.join(project_root, "connect", "bvtk-bridge", "config.json")
    
    config = {
        "project_root": project_root,
        "inbox_dir": os.path.join(project_root, "connect", "bvtk-bridge", "inbox"),
        "processed_dir": os.path.join(project_root, "connect", "bvtk-bridge", "processed"),
        "failed_dir": os.path.join(project_root, "connect", "bvtk-bridge", "failed"),
        "auto_import": True,
        "import_delay": 1.0,
        "supported_formats": ["bvtk_tree", "blender_actions"]
    }
    
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 创建配置文件: {config_path}")
    return config_path

def create_openwebui_config():
    """创建 Open WebUI 配置文件"""
    project_root = os.environ.get("CONNECT_PROJECT_ROOT", "/home/kazure/Developments/simulation/final")
    
    # 创建 Open WebUI 配置目录
    openwebui_config_dir = os.path.join(project_root, "connect", "open-webui-actions")
    os.makedirs(openwebui_config_dir, exist_ok=True)
    
    # 创建环境变量文件
    env_file = os.path.join(openwebui_config_dir, ".env")
    with open(env_file, "w", encoding="utf-8") as f:
        f.write(f"CONNECT_PROJECT_ROOT={project_root}\n")
        f.write(f"BVTK_INBOX_DIR={os.path.join(project_root, 'connect', 'bvtk-bridge', 'inbox')}\n")
        f.write(f"BVTK_PROCESSED_DIR={os.path.join(project_root, 'connect', 'bvtk-bridge', 'processed')}\n")
        f.write(f"BVTK_FAILED_DIR={os.path.join(project_root, 'connect', 'bvtk-bridge', 'failed')}\n")
    
    print(f"✓ 创建环境变量文件: {env_file}")
    
    # 创建启动脚本
    startup_script = os.path.join(openwebui_config_dir, "start_openwebui.sh")
    with open(startup_script, "w", encoding="utf-8") as f:
        f.write(f"""#!/bin/bash
# Open WebUI 启动脚本（包含 BVtkNodes Action Functions）

export CONNECT_PROJECT_ROOT={project_root}
export BVTK_INBOX_DIR={os.path.join(project_root, 'connect', 'bvtk-bridge', 'inbox')}

# 启动 Open WebUI
cd {project_root}/open-webui
python -m openwebui.serve --host 0.0.0.0 --port 8080
""")
    
    os.chmod(startup_script, 0o755)
    print(f"✓ 创建启动脚本: {startup_script}")
    
    return openwebui_config_dir

def create_test_data():
    """创建测试数据"""
    project_root = os.environ.get("CONNECT_PROJECT_ROOT", "/home/kazure/Developments/simulation/final")
    inbox_dir = os.path.join(project_root, "connect", "bvtk-bridge", "inbox")
    
    # 创建测试用的 BVtkNodes JSON
    test_bvtk_json = {
        "nodes": [
            {
                "bl_idname": "VTKSphereSourceType",
                "name": "vtkSphereSource",
                "location": [0, 0],
                "m_Radius": 1.0,
                "m_Center": [0, 0, 0],
                "m_PhiResolution": 20,
                "m_ThetaResolution": 20
            },
            {
                "bl_idname": "BVTK_Node_VTKToBlenderMeshType",
                "name": "VTK To Blender Mesh",
                "location": [300, 0],
                "m_Name": "TestSphere",
                "generate_material": True
            }
        ],
        "links": [
            {
                "from_node_name": "vtkSphereSource",
                "from_socket_identifier": "output",
                "to_node_name": "VTK To Blender Mesh",
                "to_socket_identifier": "input"
            }
        ]
    }
    
    test_file = os.path.join(inbox_dir, "test_bvtk_sphere.json")
    with open(test_file, "w", encoding="utf-8") as f:
        json.dump(test_bvtk_json, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 创建测试文件: {test_file}")
    
    # 创建测试用的 Blender 动作 JSON
    test_actions_json = {
        "version": 1,
        "doc": "测试 Blender 动作",
        "actions": [
            {
                "type": "create_object",
                "object_type": "MESH",
                "primitive": "CUBE",
                "name": "TestCube",
                "location": [0, 0, 0],
                "scale": [2, 2, 2]
            },
            {
                "type": "add_modifier",
                "object": "TestCube",
                "modifier": "SUBSURF",
                "levels": 2
            }
        ]
    }
    
    test_actions_file = os.path.join(inbox_dir, "test_blender_actions.json")
    with open(test_actions_file, "w", encoding="utf-8") as f:
        json.dump(test_actions_json, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 创建测试动作文件: {test_actions_file}")

def create_blender_addon():
    """创建 Blender 自动加载插件"""
    project_root = os.environ.get("CONNECT_PROJECT_ROOT", "/home/kazure/Developments/simulation/final")
    addon_dir = os.path.join(project_root, "connect", "blender-bridge")
    os.makedirs(addon_dir, exist_ok=True)
    
    # 创建自动加载插件
    addon_file = os.path.join(addon_dir, "bvtk_autoload_addon.py")
    addon_content = '''bl_info = {
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
'''
    
    with open(addon_file, "w", encoding="utf-8") as f:
        f.write(addon_content)
    
    print(f"✓ 创建 Blender 插件: {addon_file}")

def main():
    """主函数"""
    print("Open WebUI Action Functions 设置脚本")
    print("="*50)
    
    # 设置目录
    print("\n1. 设置目录结构...")
    setup_directories()
    
    # 创建配置文件
    print("\n2. 创建配置文件...")
    create_config_file()
    
    # 创建 Open WebUI 配置
    print("\n3. 创建 Open WebUI 配置...")
    create_openwebui_config()
    
    # 创建测试数据
    print("\n4. 创建测试数据...")
    create_test_data()
    
    # 创建 Blender 插件
    print("\n5. 创建 Blender 插件...")
    create_blender_addon()
    
    print("\n" + "="*50)
    print("设置完成！")
    print("\n下一步:")
    print("1. 在 Blender 中安装 bvtk_autoload_addon.py 插件")
    print("2. 启动 Open WebUI 并配置 Action Functions")
    print("3. 测试 JSON 提取和导入功能")
    print("\n测试命令:")
    print("cd /home/kazure/Developments/simulation/final/connect/open-webui-actions")
    print("python example_usage.py")

if __name__ == "__main__":
    main()
