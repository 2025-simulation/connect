#!/usr/bin/env python3
"""
测试独立版本的 Open WebUI Action Functions
"""

import sys
from pathlib import Path

# 添加当前目录到 Python 路径
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def test_standalone_functions():
    """测试独立版本的 Function 类"""
    print("=== 测试独立版本的 Function 类 ===")
    
    try:
        from openwebui_functions_standalone import Function
        print("✓ Function 类导入成功")
        
        # 测试基本功能
        print("\n--- 测试 extract_bvtk_json ---")
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
        
        result = Function.extract_bvtk_json(test_text, "test_standalone")
        print(f"提取结果: {result['success']}")
        if result['success']:
            print(f"  - 文件路径: {result['filepath']}")
            print(f"  - JSON 类型: {result['json_type']}")
        
        print("\n--- 测试 create_bvtk_sphere ---")
        result = Function.create_bvtk_sphere(radius=3.0, center=[1, 2, 3])
        print(f"创建球体: {result['success']}")
        if result['success']:
            print(f"  - 文件路径: {result['filepath']}")
            print(f"  - 节点数量: {result['node_count']}")
        
        print("\n--- 测试 list_inbox_files ---")
        result = Function.list_inbox_files()
        print(f"列出文件: {result['success']}")
        if result['success']:
            print(f"  - 文件数量: {result['count']}")
        
        print("\n--- 测试 get_system_status ---")
        result = Function.get_system_status()
        print(f"系统状态: {result['success']}")
        if result['success']:
            status = result['status']
            print(f"  - 收件箱文件: {status['inbox_files']}")
            print(f"  - 已处理文件: {status['processed_files']}")
            print(f"  - 失败文件: {status['failed_files']}")
        
        return True
        
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主函数"""
    print("独立版本 Open WebUI Action Functions 测试")
    print("="*50)
    
    if test_standalone_functions():
        print("\n🎉 所有测试通过！")
        print("\n下一步:")
        print("1. 将 openwebui_functions_standalone.py 复制到 Open WebUI 的 functions 目录")
        print("2. 将 actions.json 复制到 Open WebUI 的 functions 目录")
        print("3. 在 Open WebUI 中启用这些 Action Functions")
    else:
        print("\n⚠️ 测试失败，请检查错误信息")

if __name__ == "__main__":
    main()
