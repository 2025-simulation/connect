#!/usr/bin/env python3
"""
Open WebUI Action Functions 使用示例
演示如何在 Open WebUI 中集成 BVtkNodes JSON 处理功能
"""

import json
import os
from pathlib import Path

# 模拟 Open WebUI 的 Action Functions 调用
def simulate_openwebui_actions():
    """模拟 Open WebUI 中的 Action Functions 调用"""
    
    # 示例 1: 从 AI 输出中提取 JSON
    ai_output = """
    根据您的需求，我生成了以下 BVtkNodes 节点树配置：
    
    ```json
    {
      "nodes": [
        {
          "bl_idname": "VTKSphereSourceType",
          "name": "vtkSphereSource",
          "location": [0, 0],
          "m_Radius": 2.0,
          "m_Center": [0, 0, 0],
          "m_PhiResolution": 20,
          "m_ThetaResolution": 20
        },
        {
          "bl_idname": "BVTK_Node_VTKToBlenderMeshType",
          "name": "VTK To Blender Mesh",
          "location": [300, 0],
          "m_Name": "SphereMesh",
          "generate_material": true
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
    ```
    
    这个配置创建了一个球体源节点，并将其连接到 Blender 网格输出节点。
    """
    
    print("=== 示例 1: 从 AI 输出提取 JSON ===")
    
    # 调用 extract_bvtk_json Action Function
    try:
        from bvtk_json_extractor import extract_and_save_bvtk_json
        result = extract_and_save_bvtk_json(ai_output, "example")
        print(f"提取结果: {json.dumps(result, ensure_ascii=False, indent=2)}")
    except Exception as e:
        print(f"提取失败: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # 示例 2: 列出收件箱文件
    print("=== 示例 2: 列出收件箱文件 ===")
    
    try:
        from bvtk_json_extractor import list_inbox_files
        result = list_inbox_files()
        print(f"收件箱文件: {json.dumps(result, ensure_ascii=False, indent=2)}")
    except Exception as e:
        print(f"列出文件失败: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # 示例 3: 创建 Blender 动作计划 JSON
    blender_actions = {
        "version": 1,
        "doc": "创建基础几何体场景",
        "actions": [
            {
                "type": "create_object",
                "object_type": "MESH",
                "primitive": "CUBE",
                "name": "BaseCube",
                "location": [0, 0, 0],
                "scale": [2, 2, 2]
            },
            {
                "type": "create_object",
                "object_type": "MESH",
                "primitive": "UV_SPHERE",
                "name": "Sphere",
                "location": [5, 0, 0],
                "scale": [1.5, 1.5, 1.5]
            },
            {
                "type": "add_modifier",
                "object": "BaseCube",
                "modifier": "SUBSURF",
                "levels": 2
            },
            {
                "type": "set_shade_smooth",
                "object": "Sphere"
            }
        ]
    }
    
    print("=== 示例 3: 创建 Blender 动作计划 ===")
    
    try:
        from bvtk_json_extractor import extract_and_save_bvtk_json
        actions_text = json.dumps(blender_actions, ensure_ascii=False, indent=2)
        result = extract_and_save_bvtk_json(actions_text, "blender_actions")
        print(f"动作计划保存结果: {json.dumps(result, ensure_ascii=False, indent=2)}")
    except Exception as e:
        print(f"保存动作计划失败: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # 示例 4: 批量处理收件箱文件
    print("=== 示例 4: 批量处理收件箱文件 ===")
    
    try:
        from bvtk_json_extractor import process_all_inbox_files
        result = process_all_inbox_files()
        print(f"批量处理结果: {json.dumps(result, ensure_ascii=False, indent=2)}")
    except Exception as e:
        print(f"批量处理失败: {e}")


def create_openwebui_integration_guide():
    """创建 Open WebUI 集成指南"""
    
    guide = """
# Open WebUI 集成指南

## 1. 安装 Action Functions

将以下文件复制到 Open WebUI 的 actions 目录：

```
open-webui-actions/
├── actions.json
├── action_functions.py
└── bvtk_json_extractor.py
```

## 2. 配置 Open WebUI

在 Open WebUI 管理界面中：

1. 进入 Settings > Functions
2. 启用以下 Action Functions：
   - `extract_bvtk_json`
   - `import_bvtk_json_to_blender`
   - `list_inbox_files`
   - `process_all_inbox_files`

## 3. 在对话中使用

### 方法 1: 直接调用 Action Functions

在对话中，AI 可以自动调用这些函数：

```
用户: 请生成一个球体的 BVtkNodes 配置

AI: 我来为您生成球体的 BVtkNodes 配置...

[AI 生成 JSON 配置]

[自动调用 extract_bvtk_json 保存到收件箱]
[自动调用 import_bvtk_json_to_blender 导入到 Blender]
```

### 方法 2: 手动调用

用户也可以手动调用这些函数：

```
用户: 请处理收件箱中的所有文件

AI: [调用 process_all_inbox_files 函数]
```

## 4. 工作流程

1. **AI 生成 JSON**: AI 根据用户需求生成 BVtkNodes 或 Blender 动作 JSON
2. **自动提取**: 系统自动检测并提取 JSON 数据
3. **保存到收件箱**: JSON 文件保存到 `bvtk-bridge/inbox/` 目录
4. **导入 Blender**: 自动将 JSON 导入到 Blender 中
5. **文件管理**: 处理完成后移动到 `processed/` 或 `failed/` 目录

## 5. 监控和调试

- 使用 `list_inbox_files` 查看待处理文件
- 检查 `bvtk-bridge/failed/` 目录中的错误文件
- 查看 Blender 控制台输出获取详细错误信息

## 6. 自定义配置

可以通过环境变量自定义路径：

```bash
export CONNECT_PROJECT_ROOT="/path/to/your/project"
export BVTK_INBOX_DIR="/path/to/custom/inbox"
```
"""
    
    with open("/home/kazure/Developments/simulation/final/connect/open-webui-actions/INTEGRATION_GUIDE.md", "w", encoding="utf-8") as f:
        f.write(guide)
    
    print("集成指南已创建: INTEGRATION_GUIDE.md")


if __name__ == "__main__":
    print("Open WebUI Action Functions 使用示例")
    print("="*50)
    
    # 运行示例
    simulate_openwebui_actions()
    
    # 创建集成指南
    create_openwebui_integration_guide()
    
    print("\n示例运行完成！")
    print("请查看 INTEGRATION_GUIDE.md 了解详细的集成步骤。")
