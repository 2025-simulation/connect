#!/usr/bin/env python3
"""
不依赖 Blender 的测试脚本
测试 JSON 提取和文件管理功能
"""

import json
import os
import sys
from pathlib import Path

# 添加当前目录到 Python 路径
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def test_json_extraction():
    """测试 JSON 提取功能"""
    print("=== 测试 JSON 提取功能 ===")
    
    # 模拟 AI 输出
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
    
    # 导入 JSON 提取函数（不依赖 bpy）
    try:
        from bvtk_json_extractor import extract_json_from_text, detect_bvtk_json_type, save_json_to_inbox
        
        # 提取 JSON
        json_data = extract_json_from_text(ai_output)
        if json_data:
            print(f"✓ 成功提取 JSON 数据")
            print(f"  - JSON 类型: {detect_bvtk_json_type(json_data)}")
            print(f"  - 节点数量: {len(json_data.get('nodes', []))}")
            print(f"  - 连接数量: {len(json_data.get('links', []))}")
            
            # 保存到收件箱
            filepath = save_json_to_inbox(json_data, "test_extraction")
            print(f"✓ 保存到收件箱: {filepath}")
            
            return True
        else:
            print("✗ 未能提取 JSON 数据")
            return False
            
    except Exception as e:
        print(f"✗ 提取失败: {e}")
        return False

def test_file_management():
    """测试文件管理功能"""
    print("\n=== 测试文件管理功能 ===")
    
    try:
        from bvtk_json_extractor import list_inbox_files, move_file_to_processed, move_file_to_failed
        
        # 列出收件箱文件
        result = list_inbox_files()
        if result["success"]:
            print(f"✓ 收件箱文件数量: {result['count']}")
            for file_info in result["files"]:
                print(f"  - {file_info['filename']} ({file_info['size']} bytes)")
        else:
            print(f"✗ 列出文件失败: {result['message']}")
            return False
        
        # 测试文件移动（如果有文件的话）
        if result["files"]:
            first_file = result["files"][0]["filepath"]
            print(f"\n测试移动文件: {first_file}")
            
            # 移动到已处理目录
            processed_path = move_file_to_processed(first_file)
            print(f"✓ 移动到已处理目录: {processed_path}")
            
            # 移动回收件箱（用于测试）
            import shutil
            shutil.move(processed_path, first_file)
            print(f"✓ 移回收件箱: {first_file}")
        
        return True
        
    except Exception as e:
        print(f"✗ 文件管理测试失败: {e}")
        return False

def test_blender_actions():
    """测试 Blender 动作计划"""
    print("\n=== 测试 Blender 动作计划 ===")
    
    # 创建 Blender 动作计划
    blender_actions = {
        "version": 1,
        "doc": "创建基础几何体场景",
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
            },
            {
                "type": "set_shade_smooth",
                "object": "TestCube"
            }
        ]
    }
    
    try:
        from bvtk_json_extractor import detect_bvtk_json_type, save_json_to_inbox
        
        # 检测 JSON 类型
        json_type = detect_bvtk_json_type(blender_actions)
        print(f"✓ JSON 类型: {json_type}")
        
        # 保存到收件箱
        filepath = save_json_to_inbox(blender_actions, "test_actions")
        print(f"✓ 保存动作计划: {filepath}")
        
        # 验证保存的文件
        with open(filepath, 'r', encoding='utf-8') as f:
            saved_data = json.load(f)
        
        print(f"✓ 验证保存的数据:")
        print(f"  - 版本: {saved_data.get('version')}")
        print(f"  - 动作数量: {len(saved_data.get('actions', []))}")
        print(f"  - 文档: {saved_data.get('doc')}")
        
        return True
        
    except Exception as e:
        print(f"✗ 动作计划测试失败: {e}")
        return False

def test_json_detection():
    """测试 JSON 类型检测"""
    print("\n=== 测试 JSON 类型检测 ===")
    
    # 测试 BVtkNodes 节点树 JSON
    bvtk_json = {
        "nodes": [
            {"bl_idname": "VTKSphereSourceType", "name": "sphere"}
        ],
        "links": [
            {"from_node_name": "sphere", "to_node_name": "output"}
        ]
    }
    
    # 测试 Blender 动作计划 JSON
    actions_json = {
        "version": 1,
        "actions": [
            {"type": "create_object", "primitive": "CUBE"}
        ]
    }
    
    # 测试未知类型 JSON
    unknown_json = {
        "some_field": "some_value"
    }
    
    try:
        from bvtk_json_extractor import detect_bvtk_json_type
        
        print(f"✓ BVtkNodes 节点树: {detect_bvtk_json_type(bvtk_json)}")
        print(f"✓ Blender 动作计划: {detect_bvtk_json_type(actions_json)}")
        print(f"✓ 未知类型: {detect_bvtk_json_type(unknown_json)}")
        
        return True
        
    except Exception as e:
        print(f"✗ 类型检测测试失败: {e}")
        return False

def main():
    """主函数"""
    print("Open WebUI Action Functions 测试（不依赖 Blender）")
    print("="*60)
    
    tests = [
        ("JSON 提取", test_json_extraction),
        ("文件管理", test_file_management),
        ("Blender 动作计划", test_blender_actions),
        ("JSON 类型检测", test_json_detection),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            if test_func():
                passed += 1
                print(f"✓ {test_name} 测试通过")
            else:
                print(f"✗ {test_name} 测试失败")
        except Exception as e:
            print(f"✗ {test_name} 测试异常: {e}")
    
    print(f"\n{'='*60}")
    print(f"测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！")
    else:
        print("⚠️  部分测试失败，请检查错误信息")
    
    print(f"\n下一步:")
    print(f"1. 在 Blender 中安装 bvtk_autoload_addon.py 插件")
    print(f"2. 启动 Open WebUI 并配置 Action Functions")
    print(f"3. 测试完整的 JSON 提取和导入流程")

if __name__ == "__main__":
    main()
