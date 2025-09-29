#!/usr/bin/env python3
"""
测试 Open WebUI Action Functions
验证所有 Action Functions 是否正常工作
"""

import json
import sys
from pathlib import Path

# 添加当前目录到 Python 路径
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def test_function_class():
    """测试 Function 类是否存在"""
    print("=== 测试 Function 类 ===")
    
    try:
        from openwebui_functions import Function
        print("✓ Function 类导入成功")
        
        # 检查是否有必要的方法
        required_methods = [
            'extract_bvtk_json',
            'import_bvtk_json_to_blender',
            'list_inbox_files',
            'process_all_inbox_files',
            'create_bvtk_sphere',
            'create_blender_cube',
            'get_system_status'
        ]
        
        for method_name in required_methods:
            if hasattr(Function, method_name):
                print(f"✓ 方法 {method_name} 存在")
            else:
                print(f"✗ 方法 {method_name} 不存在")
                return False
        
        return True
        
    except Exception as e:
        print(f"✗ 导入 Function 类失败: {e}")
        return False

def test_extract_bvtk_json():
    """测试 extract_bvtk_json 方法"""
    print("\n=== 测试 extract_bvtk_json ===")
    
    try:
        from openwebui_functions import Function
        
        # 测试文本
        test_text = """
        根据您的需求，我生成了以下 BVtkNodes 节点树配置：
        
        ```json
        {
          "nodes": [
            {
              "bl_idname": "VTKSphereSourceType",
              "name": "vtkSphereSource",
              "location": [0, 0],
              "m_Radius": 2.0,
              "m_Center": [0, 0, 0]
            }
          ],
          "links": []
        }
        ```
        """
        
        result = Function.extract_bvtk_json(test_text, "test")
        
        if result["success"]:
            print(f"✓ 提取成功: {result['message']}")
            print(f"  - 文件路径: {result['filepath']}")
            print(f"  - JSON 类型: {result['json_type']}")
            return True
        else:
            print(f"✗ 提取失败: {result['message']}")
            return False
            
    except Exception as e:
        print(f"✗ 测试异常: {e}")
        return False

def test_create_bvtk_sphere():
    """测试 create_bvtk_sphere 方法"""
    print("\n=== 测试 create_bvtk_sphere ===")
    
    try:
        from openwebui_functions import Function
        
        result = Function.create_bvtk_sphere(radius=2.5, center=[1, 2, 3], resolution=30)
        
        if result["success"]:
            print(f"✓ 创建球体成功: {result['message']}")
            print(f"  - 文件路径: {result['filepath']}")
            print(f"  - 节点数量: {result['node_count']}")
            print(f"  - 连接数量: {result['link_count']}")
            return True
        else:
            print(f"✗ 创建球体失败: {result['message']}")
            return False
            
    except Exception as e:
        print(f"✗ 测试异常: {e}")
        return False

def test_create_blender_cube():
    """测试 create_blender_cube 方法"""
    print("\n=== 测试 create_blender_cube ===")
    
    try:
        from openwebui_functions import Function
        
        result = Function.create_blender_cube(name="TestCube", location=[5, 5, 5], scale=[2, 2, 2])
        
        if result["success"]:
            print(f"✓ 创建立方体成功: {result['message']}")
            print(f"  - 文件路径: {result['filepath']}")
            print(f"  - 动作数量: {result['action_count']}")
            return True
        else:
            print(f"✗ 创建立方体失败: {result['message']}")
            return False
            
    except Exception as e:
        print(f"✗ 测试异常: {e}")
        return False

def test_list_inbox_files():
    """测试 list_inbox_files 方法"""
    print("\n=== 测试 list_inbox_files ===")
    
    try:
        from openwebui_functions import Function
        
        result = Function.list_inbox_files()
        
        if result["success"]:
            message = result.get('message', '列出文件成功')
            print(f"✓ 列出文件成功: {message}")
            print(f"  - 文件数量: {result['count']}")
            for file_info in result["files"][:3]:  # 只显示前3个文件
                print(f"    - {file_info['filename']} ({file_info['size']} bytes)")
            return True
        else:
            message = result.get('message', '未知错误')
            print(f"✗ 列出文件失败: {message}")
            return False
            
    except Exception as e:
        print(f"✗ 测试异常: {e}")
        return False

def test_get_system_status():
    """测试 get_system_status 方法"""
    print("\n=== 测试 get_system_status ===")
    
    try:
        from openwebui_functions import Function
        
        result = Function.get_system_status()
        
        if result["success"]:
            print(f"✓ 获取系统状态成功: {result['message']}")
            status = result["status"]
            print(f"  - 项目根目录: {status['project_root']}")
            print(f"  - 收件箱文件: {status['inbox_files']}")
            print(f"  - 已处理文件: {status['processed_files']}")
            print(f"  - 失败文件: {status['failed_files']}")
            print(f"  - 总文件数: {status['total_files']}")
            return True
        else:
            print(f"✗ 获取系统状态失败: {result['message']}")
            return False
            
    except Exception as e:
        print(f"✗ 测试异常: {e}")
        return False

def test_import_bvtk_json():
    """测试 import_bvtk_json_to_blender 方法"""
    print("\n=== 测试 import_bvtk_json_to_blender ===")
    
    try:
        from openwebui_functions import Function
        
        # 先创建一个测试文件
        test_file = "/home/kazure/Developments/simulation/final/connect/bvtk-bridge/inbox/test_import.json"
        test_data = {
            "nodes": [
                {
                    "bl_idname": "VTKSphereSourceType",
                    "name": "test_sphere",
                    "location": [0, 0],
                    "m_Radius": 1.0
                }
            ],
            "links": []
        }
        
        with open(test_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f, ensure_ascii=False, indent=2)
        
        result = Function.import_bvtk_json_to_blender(test_file)
        
        if result["success"]:
            print(f"✓ 导入成功: {result['message']}")
            if 'simulated' in result:
                print("  - [模拟模式] 实际 Blender 环境中会执行真实导入")
            return True
        else:
            print(f"✗ 导入失败: {result['message']}")
            return False
            
    except Exception as e:
        print(f"✗ 测试异常: {e}")
        return False

def main():
    """主函数"""
    print("Open WebUI Action Functions 测试")
    print("="*50)
    
    tests = [
        ("Function 类检查", test_function_class),
        ("extract_bvtk_json", test_extract_bvtk_json),
        ("create_bvtk_sphere", test_create_bvtk_sphere),
        ("create_blender_cube", test_create_blender_cube),
        ("list_inbox_files", test_list_inbox_files),
        ("get_system_status", test_get_system_status),
        ("import_bvtk_json_to_blender", test_import_bvtk_json),
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
    
    print(f"\n{'='*50}")
    print(f"测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！")
        print("\n下一步:")
        print("1. 将 openwebui_functions.py 复制到 Open WebUI 的 functions 目录")
        print("2. 将 actions.json 复制到 Open WebUI 的 functions 目录")
        print("3. 在 Open WebUI 中启用这些 Action Functions")
        print("4. 测试与 AI 的交互")
    else:
        print("⚠️  部分测试失败，请检查错误信息")

if __name__ == "__main__":
    main()
