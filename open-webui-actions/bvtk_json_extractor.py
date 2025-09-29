"""
Open WebUI Action Functions for BVtkNodes JSON Processing
用于从 AI 输出中提取 BVtkNodes JSON 并自动导入到 Blender 的 Action Functions
"""

import json
import os
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Union

# 尝试导入 Blender 模块，如果不可用则提供占位符
try:
    import bpy
    import bmesh
    from mathutils import Vector
    BLENDER_AVAILABLE = True
except ImportError:
    BLENDER_AVAILABLE = False
    # 提供占位符类
    class MockBpy:
        class context:
            class view_layer:
                objects = {}
            class area:
                type = 'NODE_EDITOR'
            class space_data:
                node_tree = None
        class data:
            class objects:
                @staticmethod
                def get(name): return None
            class node_groups:
                @staticmethod
                def new(name, type): return None
                def get(name): return None
            class collections:
                @staticmethod
                def get(name): return None
            class textures:
                @staticmethod
                def new(name, type): return None
        class ops:
            class mesh:
                @staticmethod
                def primitive_cube_add(**kwargs): pass
                @staticmethod
                def primitive_plane_add(**kwargs): pass
                @staticmethod
                def primitive_uv_sphere_add(**kwargs): pass
                @staticmethod
                def select_all(action): pass
                @staticmethod
                def faces_shade_smooth(): pass
            class object:
                @staticmethod
                def mode_set(mode): pass
            class import_scene:
                @staticmethod
                def obj(filepath): pass
                @staticmethod
                def fbx(filepath): pass
                @staticmethod
                def gltf(filepath): pass
        class app:
            class timers:
                @staticmethod
                def register(func, **kwargs): pass
    
    bpy = MockBpy()
    bmesh = None
    Vector = None

# 配置路径
PROJECT_ROOT = os.environ.get("CONNECT_PROJECT_ROOT", "/home/kazure/Developments/simulation/final")
BVTK_INBOX_DIR = os.path.join(PROJECT_ROOT, "connect", "bvtk-bridge", "inbox")
BVTK_PROCESSED_DIR = os.path.join(PROJECT_ROOT, "connect", "bvtk-bridge", "processed")
BVTK_FAILED_DIR = os.path.join(PROJECT_ROOT, "connect", "bvtk-bridge", "failed")

# 确保目录存在
for dir_path in [BVTK_INBOX_DIR, BVTK_PROCESSED_DIR, BVTK_FAILED_DIR]:
    os.makedirs(dir_path, exist_ok=True)


def extract_json_from_text(text: str) -> Optional[Dict[str, Any]]:
    """
    从文本中提取 JSON 数据
    
    Args:
        text: 包含 JSON 的文本
        
    Returns:
        解析后的 JSON 字典，如果未找到则返回 None
    """
    # 方法1: 查找代码块中的 JSON
    json_patterns = [
        r'```json\s*\n(.*?)\n```',
        r'```JSON\s*\n(.*?)\n```',
        r'```\s*\n(.*?)\n```'
    ]
    
    for pattern in json_patterns:
        matches = re.findall(pattern, text, re.DOTALL)
        for match in matches:
            try:
                return json.loads(match.strip())
            except json.JSONDecodeError:
                continue
    
    # 方法2: 查找大括号包围的 JSON
    try:
        start = text.find('{')
        if start != -1:
            # 找到匹配的结束大括号
            brace_count = 0
            for i, char in enumerate(text[start:], start):
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        json_str = text[start:i+1]
                        return json.loads(json_str)
    except json.JSONDecodeError:
        pass
    
    return None


def detect_bvtk_json_type(json_data: Dict[str, Any]) -> str:
    """
    检测 JSON 类型
    
    Args:
        json_data: JSON 数据
        
    Returns:
        JSON 类型: 'bvtk_tree', 'blender_actions', 'unknown'
    """
    if not isinstance(json_data, dict):
        return 'unknown'
    
    # 检测 BVtkNodes 节点树 JSON
    if 'nodes' in json_data and 'links' in json_data:
        if isinstance(json_data['nodes'], list) and isinstance(json_data['links'], list):
            return 'bvtk_tree'
    
    # 检测 Blender 动作计划 JSON
    if 'actions' in json_data and isinstance(json_data['actions'], list):
        return 'blender_actions'
    
    return 'unknown'


def save_json_to_inbox(json_data: Dict[str, Any], filename_prefix: str = "bvtk") -> str:
    """
    保存 JSON 到收件箱目录
    
    Args:
        json_data: JSON 数据
        filename_prefix: 文件名前缀
        
    Returns:
        保存的文件路径
    """
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{filename_prefix}-{timestamp}.json"
    filepath = os.path.join(BVTK_INBOX_DIR, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    
    return filepath


def move_file_to_processed(filepath: str) -> str:
    """
    将文件移动到已处理目录
    
    Args:
        filepath: 源文件路径
        
    Returns:
        目标文件路径
    """
    filename = os.path.basename(filepath)
    dest_path = os.path.join(BVTK_PROCESSED_DIR, filename)
    shutil.move(filepath, dest_path)
    return dest_path


def move_file_to_failed(filepath: str, error_msg: str = "") -> str:
    """
    将文件移动到失败目录
    
    Args:
        filepath: 源文件路径
        error_msg: 错误信息
        
    Returns:
        目标文件路径
    """
    filename = os.path.basename(filepath)
    dest_path = os.path.join(BVTK_FAILED_DIR, filename)
    shutil.move(filepath, dest_path)
    
    # 保存错误信息
    if error_msg:
        error_file = dest_path + ".error.txt"
        with open(error_file, 'w', encoding='utf-8') as f:
            f.write(error_msg)
    
    return dest_path


# Open WebUI Action Functions

def extract_and_save_bvtk_json(text: str, filename_prefix: str = "bvtk") -> Dict[str, Any]:
    """
    Action Function: 从文本中提取并保存 BVtkNodes JSON
    
    Args:
        text: 包含 JSON 的文本
        filename_prefix: 文件名前缀
        
    Returns:
        操作结果
    """
    try:
        # 提取 JSON
        json_data = extract_json_from_text(text)
        if not json_data:
            return {
                "success": False,
                "message": "未在文本中找到有效的 JSON 数据",
                "filepath": None
            }
        
        # 检测 JSON 类型
        json_type = detect_bvtk_json_type(json_data)
        
        # 保存到收件箱
        filepath = save_json_to_inbox(json_data, filename_prefix)
        
        return {
            "success": True,
            "message": f"成功提取并保存 {json_type} JSON 到收件箱",
            "filepath": filepath,
            "json_type": json_type,
            "node_count": len(json_data.get('nodes', [])) if json_type == 'bvtk_tree' else None,
            "action_count": len(json_data.get('actions', [])) if json_type == 'blender_actions' else None
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"提取 JSON 时发生错误: {str(e)}",
            "filepath": None
        }


def import_bvtk_json_to_blender(filepath: str) -> Dict[str, Any]:
    """
    Action Function: 将 BVtkNodes JSON 导入到 Blender
    
    Args:
        filepath: JSON 文件路径
        
    Returns:
        操作结果
    """
    try:
        # 读取 JSON 文件
        with open(filepath, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        json_type = detect_bvtk_json_type(json_data)
        
        if json_type == 'bvtk_tree':
            # 导入 BVtkNodes 节点树
            result = import_bvtk_node_tree(json_data)
        elif json_type == 'blender_actions':
            # 执行 Blender 动作计划
            result = execute_blender_actions(json_data)
        else:
            return {
                "success": False,
                "message": f"不支持的 JSON 类型: {json_type}",
                "filepath": filepath
            }
        
        if result["success"]:
            # 移动到已处理目录
            processed_path = move_file_to_processed(filepath)
            result["processed_path"] = processed_path
        else:
            # 移动到失败目录
            failed_path = move_file_to_failed(filepath, result.get("message", ""))
            result["failed_path"] = failed_path
        
        return result
        
    except Exception as e:
        error_msg = f"导入 JSON 时发生错误: {str(e)}"
        failed_path = move_file_to_failed(filepath, error_msg)
        return {
            "success": False,
            "message": error_msg,
            "failed_path": failed_path
        }


def import_bvtk_node_tree(json_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    导入 BVtkNodes 节点树到 Blender
    
    Args:
        json_data: 包含 nodes 和 links 的 JSON 数据
        
    Returns:
        操作结果
    """
    try:
        if not BLENDER_AVAILABLE:
            # 模拟导入过程
            nodes = json_data.get('nodes', [])
            links = json_data.get('links', [])
            return {
                "success": True,
                "message": f"[模拟] 成功导入 {len(nodes)} 个节点和 {len(links)} 个连接",
                "node_count": len(nodes),
                "link_count": len(links),
                "simulated": True
            }
        
        # 确保在节点编辑器中
        if not bpy.context.area or bpy.context.area.type != 'NODE_EDITOR':
            return {
                "success": False,
                "message": "请在节点编辑器中执行此操作"
            }
        
        # 创建或获取 BVtkNodes 节点树
        node_tree_name = "BVTK_NodeTree"
        if node_tree_name not in bpy.data.node_groups:
            node_tree = bpy.data.node_groups.new(node_tree_name, "BVTK_NodeTreeType")
        else:
            node_tree = bpy.data.node_groups[node_tree_name]
        
        # 清空现有节点
        for node in node_tree.nodes:
            node_tree.nodes.remove(node)
        
        # 导入节点
        nodes = json_data.get('nodes', [])
        links = json_data.get('links', [])
        
        # 创建节点
        node_map = {}
        for node_data in nodes:
            node = create_bvtk_node(node_tree, node_data)
            if node:
                node_map[node_data['name']] = node
        
        # 创建连接
        for link_data in links:
            create_node_link(node_tree, node_map, link_data)
        
        # 设置活动节点树
        bpy.context.space_data.node_tree = node_tree
        
        return {
            "success": True,
            "message": f"成功导入 {len(nodes)} 个节点和 {len(links)} 个连接",
            "node_count": len(nodes),
            "link_count": len(links)
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"导入节点树时发生错误: {str(e)}"
        }


def create_bvtk_node(node_tree, node_data: Dict[str, Any]):
    """
    创建 BVtkNodes 节点
    
    Args:
        node_tree: Blender 节点树
        node_data: 节点数据
        
    Returns:
        创建的节点
    """
    try:
        bl_idname = node_data.get('bl_idname')
        if not bl_idname:
            return None
        
        # 创建节点
        node = node_tree.nodes.new(bl_idname)
        
        # 设置基本属性
        if 'name' in node_data:
            node.name = node_data['name']
        if 'label' in node_data:
            node.label = node_data['label']
        if 'location' in node_data:
            node.location = node_data['location']
        if 'width' in node_data:
            node.width = node_data['width']
        if 'height' in node_data:
            node.height = node_data['height']
        
        # 设置节点特定属性
        for key, value in node_data.items():
            if hasattr(node, key) and not key in ['name', 'label', 'location', 'width', 'height', 'bl_idname']:
                try:
                    setattr(node, key, value)
                except:
                    pass  # 忽略无法设置的属性
        
        return node
        
    except Exception as e:
        print(f"创建节点时发生错误: {str(e)}")
        return None


def create_node_link(node_tree, node_map: Dict[str, Any], link_data: Dict[str, Any]):
    """
    创建节点连接
    
    Args:
        node_tree: Blender 节点树
        node_map: 节点名称到节点的映射
        link_data: 连接数据
        
    Returns:
        是否成功创建连接
    """
    try:
        from_node_name = link_data.get('from_node_name')
        to_node_name = link_data.get('to_node_name')
        from_socket_identifier = link_data.get('from_socket_identifier')
        to_socket_identifier = link_data.get('to_socket_identifier')
        
        if not all([from_node_name, to_node_name, from_socket_identifier, to_socket_identifier]):
            return False
        
        from_node = node_map.get(from_node_name)
        to_node = node_map.get(to_node_name)
        
        if not from_node or not to_node:
            return False
        
        # 查找输出和输入插槽
        from_socket = None
        to_socket = None
        
        for socket in from_node.outputs:
            if socket.identifier == from_socket_identifier:
                from_socket = socket
                break
        
        for socket in to_node.inputs:
            if socket.identifier == to_socket_identifier:
                to_socket = socket
                break
        
        if from_socket and to_socket:
            node_tree.links.new(to_socket, from_socket)
            return True
        
        return False
        
    except Exception as e:
        print(f"创建连接时发生错误: {str(e)}")
        return False


def execute_blender_actions(json_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    执行 Blender 动作计划
    
    Args:
        json_data: 包含 actions 的 JSON 数据
        
    Returns:
        操作结果
    """
    try:
        actions = json_data.get('actions', [])
        executed_count = 0
        
        if not BLENDER_AVAILABLE:
            # 模拟执行过程
            return {
                "success": True,
                "message": f"[模拟] 成功执行 {len(actions)}/{len(actions)} 个动作",
                "executed_count": len(actions),
                "total_count": len(actions),
                "simulated": True
            }
        
        for action in actions:
            if execute_blender_action(action):
                executed_count += 1
        
        return {
            "success": True,
            "message": f"成功执行 {executed_count}/{len(actions)} 个动作",
            "executed_count": executed_count,
            "total_count": len(actions)
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"执行动作时发生错误: {str(e)}"
        }


def execute_blender_action(action: Dict[str, Any]) -> bool:
    """
    执行单个 Blender 动作
    
    Args:
        action: 动作数据
        
    Returns:
        是否成功执行
    """
    try:
        if not BLENDER_AVAILABLE:
            # 模拟执行
            action_type = action.get('type')
            print(f"[模拟] 执行动作: {action_type}")
            return True
        
        action_type = action.get('type')
        
        if action_type == 'create_object':
            return create_blender_object(action)
        elif action_type == 'add_modifier':
            return add_blender_modifier(action)
        elif action_type == 'set_shade_smooth':
            return set_blender_shade_smooth(action)
        elif action_type == 'create_texture':
            return create_blender_texture(action)
        elif action_type == 'import_file':
            return import_blender_file(action)
        else:
            print(f"未知的动作类型: {action_type}")
            return False
            
    except Exception as e:
        print(f"执行动作时发生错误: {str(e)}")
        return False


def create_blender_object(action: Dict[str, Any]) -> bool:
    """创建 Blender 对象"""
    try:
        primitive = action.get('primitive', 'CUBE')
        name = action.get('name', f"Object_{primitive}")
        location = action.get('location', [0, 0, 0])
        rotation = action.get('rotation', [0, 0, 0])
        scale = action.get('scale', [1, 1, 1])
        
        # 创建基础网格
        if primitive == 'CUBE':
            bpy.ops.mesh.primitive_cube_add(location=location)
        elif primitive == 'PLANE':
            bpy.ops.mesh.primitive_plane_add(location=location)
        elif primitive == 'UV_SPHERE':
            bpy.ops.mesh.primitive_uv_sphere_add(location=location)
        else:
            return False
        
        # 获取活动对象
        obj = bpy.context.active_object
        if obj:
            obj.name = name
            obj.rotation_euler = rotation
            obj.scale = scale
        
        return True
        
    except Exception as e:
        print(f"创建对象时发生错误: {str(e)}")
        return False


def add_blender_modifier(action: Dict[str, Any]) -> bool:
    """添加 Blender 修改器"""
    try:
        object_name = action.get('object')
        modifier_type = action.get('modifier')
        
        if not object_name or not modifier_type:
            return False
        
        obj = bpy.data.objects.get(object_name)
        if not obj:
            return False
        
        # 添加修改器
        if modifier_type == 'SUBSURF':
            modifier = obj.modifiers.new(name="Subsurf", type='SUBSURF')
            levels = action.get('levels', 1)
            modifier.levels = levels
        elif modifier_type == 'DISPLACE':
            modifier = obj.modifiers.new(name="Displace", type='DISPLACE')
            strength = action.get('strength', 1.0)
            modifier.strength = strength
        else:
            return False
        
        return True
        
    except Exception as e:
        print(f"添加修改器时发生错误: {str(e)}")
        return False


def set_blender_shade_smooth(action: Dict[str, Any]) -> bool:
    """设置 Blender 对象平滑着色"""
    try:
        object_name = action.get('object')
        if not object_name:
            return False
        
        obj = bpy.data.objects.get(object_name)
        if not obj:
            return False
        
        # 进入编辑模式设置平滑着色
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.faces_shade_smooth()
        bpy.ops.object.mode_set(mode='OBJECT')
        
        return True
        
    except Exception as e:
        print(f"设置平滑着色时发生错误: {str(e)}")
        return False


def create_blender_texture(action: Dict[str, Any]) -> bool:
    """创建 Blender 纹理"""
    try:
        name = action.get('name')
        kind = action.get('kind', 'NOISE')
        
        if not name:
            return False
        
        # 创建纹理
        texture = bpy.data.textures.new(name=name, type='NOISE' if kind == 'NOISE' else 'VORONOI')
        
        # 设置参数
        params = action.get('params', {})
        for key, value in params.items():
            if hasattr(texture, key):
                setattr(texture, key, value)
        
        return True
        
    except Exception as e:
        print(f"创建纹理时发生错误: {str(e)}")
        return False


def import_blender_file(action: Dict[str, Any]) -> bool:
    """导入 Blender 文件"""
    try:
        file_path = action.get('path')
        file_kind = action.get('kind', 'OBJ')
        collection_name = action.get('into_collection')
        
        if not file_path:
            return False
        
        # 确保文件路径是绝对路径
        if not os.path.isabs(file_path):
            file_path = os.path.join(PROJECT_ROOT, file_path)
        
        if not os.path.exists(file_path):
            return False
        
        # 导入文件
        if file_kind == 'OBJ':
            bpy.ops.import_scene.obj(filepath=file_path)
        elif file_kind == 'FBX':
            bpy.ops.import_scene.fbx(filepath=file_path)
        elif file_kind == 'GLTF':
            bpy.ops.import_scene.gltf(filepath=file_path)
        elif file_kind == 'GLB':
            bpy.ops.import_scene.gltf(filepath=file_path)
        else:
            return False
        
        # 移动到指定集合
        if collection_name:
            collection = bpy.data.collections.get(collection_name)
            if collection:
                for obj in bpy.context.selected_objects:
                    # 从当前集合中移除
                    for col in obj.users_collection:
                        col.objects.unlink(obj)
                    # 添加到新集合
                    collection.objects.link(obj)
        
        return True
        
    except Exception as e:
        print(f"导入文件时发生错误: {str(e)}")
        return False


def list_inbox_files() -> Dict[str, Any]:
    """
    Action Function: 列出收件箱中的文件
    
    Returns:
        文件列表
    """
    try:
        files = []
        for filename in os.listdir(BVTK_INBOX_DIR):
            if filename.lower().endswith('.json'):
                filepath = os.path.join(BVTK_INBOX_DIR, filename)
                stat = os.stat(filepath)
                files.append({
                    "filename": filename,
                    "filepath": filepath,
                    "size": stat.st_size,
                    "modified": datetime.fromtimestamp(stat.st_mtime).isoformat()
                })
        
        return {
            "success": True,
            "files": files,
            "count": len(files)
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"列出文件时发生错误: {str(e)}",
            "files": []
        }


def process_all_inbox_files() -> Dict[str, Any]:
    """
    Action Function: 处理收件箱中的所有文件
    
    Returns:
        处理结果
    """
    try:
        results = []
        processed_count = 0
        failed_count = 0
        
        for filename in os.listdir(BVTK_INBOX_DIR):
            if not filename.lower().endswith('.json'):
                continue
            
            filepath = os.path.join(BVTK_INBOX_DIR, filename)
            result = import_bvtk_json_to_blender(filepath)
            results.append({
                "filename": filename,
                "result": result
            })
            
            if result["success"]:
                processed_count += 1
            else:
                failed_count += 1
        
        return {
            "success": True,
            "message": f"处理完成: {processed_count} 成功, {failed_count} 失败",
            "processed_count": processed_count,
            "failed_count": failed_count,
            "results": results
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"批量处理时发生错误: {str(e)}",
            "processed_count": 0,
            "failed_count": 0,
            "results": []
        }
