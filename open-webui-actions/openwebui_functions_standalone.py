"""
Open WebUI Action Functions for BVtkNodes - Standalone Version
独立版本，不依赖外部模块
"""

import json
import os
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional

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


class Function:
    """Open WebUI Action Functions 类"""
    
    @staticmethod
    def extract_bvtk_json(text: str, filename_prefix: str = "bvtk") -> Dict[str, Any]:
        """
        从 AI 输出文本中提取 BVtkNodes JSON 数据并保存到收件箱
        
        Args:
            text: 包含 JSON 数据的文本
            filename_prefix: 文件名前缀，默认为 "bvtk"
            
        Returns:
            操作结果字典
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

    @staticmethod
    def import_bvtk_json_to_blender(filepath: str) -> Dict[str, Any]:
        """
        将 BVtkNodes JSON 文件导入到 Blender 中
        
        Args:
            filepath: JSON 文件的完整路径
            
        Returns:
            操作结果字典
        """
        try:
            # 读取 JSON 文件
            with open(filepath, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            
            json_type = detect_bvtk_json_type(json_data)
            
            if json_type == 'bvtk_tree':
                # 模拟导入 BVtkNodes 节点树
                nodes = json_data.get('nodes', [])
                links = json_data.get('links', [])
                result = {
                    "success": True,
                    "message": f"[模拟] 成功导入 {len(nodes)} 个节点和 {len(links)} 个连接",
                    "node_count": len(nodes),
                    "link_count": len(links),
                    "simulated": True
                }
            elif json_type == 'blender_actions':
                # 模拟执行 Blender 动作计划
                actions = json_data.get('actions', [])
                result = {
                    "success": True,
                    "message": f"[模拟] 成功执行 {len(actions)} 个动作",
                    "executed_count": len(actions),
                    "total_count": len(actions),
                    "simulated": True
                }
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

    @staticmethod
    def list_inbox_files() -> Dict[str, Any]:
        """
        列出收件箱中的所有 JSON 文件
        
        Returns:
            文件列表字典
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

    @staticmethod
    def process_all_inbox_files() -> Dict[str, Any]:
        """
        批量处理收件箱中的所有 JSON 文件
        
        Returns:
            处理结果字典
        """
        try:
            results = []
            processed_count = 0
            failed_count = 0
            
            for filename in os.listdir(BVTK_INBOX_DIR):
                if not filename.lower().endswith('.json'):
                    continue
                
                filepath = os.path.join(BVTK_INBOX_DIR, filename)
                result = Function.import_bvtk_json_to_blender(filepath)
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

    @staticmethod
    def create_bvtk_sphere(radius: float = 1.0, center: List[float] = None, resolution: int = 20) -> Dict[str, Any]:
        """
        创建一个球体的 BVtkNodes 配置
        
        Args:
            radius: 球体半径
            center: 球体中心坐标 [x, y, z]
            resolution: 球体分辨率
            
        Returns:
            操作结果字典
        """
        try:
            if center is None:
                center = [0, 0, 0]
            
            # 创建球体配置
            sphere_config = {
                "nodes": [
                    {
                        "bl_idname": "VTKSphereSourceType",
                        "name": "vtkSphereSource",
                        "location": [0, 0],
                        "m_Radius": radius,
                        "m_Center": center,
                        "m_PhiResolution": resolution,
                        "m_ThetaResolution": resolution
                    },
                    {
                        "bl_idname": "BVTK_Node_VTKToBlenderMeshType",
                        "name": "VTK To Blender Mesh",
                        "location": [300, 0],
                        "m_Name": f"Sphere_{radius}",
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
            
            # 保存到收件箱
            filepath = save_json_to_inbox(sphere_config, "sphere")
            
            return {
                "success": True,
                "message": f"成功创建球体配置 (半径: {radius})",
                "filepath": filepath,
                "json_type": "bvtk_tree",
                "node_count": 2,
                "link_count": 1
            }
            
        except Exception as e:
            return {
                "success": False,
                "message": f"创建球体配置时发生错误: {str(e)}",
                "filepath": None
            }

    @staticmethod
    def create_blender_cube(name: str = "MyCube", location: List[float] = None, scale: List[float] = None) -> Dict[str, Any]:
        """
        创建一个立方体的 Blender 动作计划
        
        Args:
            name: 立方体名称
            location: 位置坐标 [x, y, z]
            scale: 缩放比例 [sx, sy, sz]
            
        Returns:
            操作结果字典
        """
        try:
            if location is None:
                location = [0, 0, 0]
            if scale is None:
                scale = [1, 1, 1]
            
            # 创建动作计划
            actions_plan = {
                "version": 1,
                "doc": f"创建立方体: {name}",
                "actions": [
                    {
                        "type": "create_object",
                        "object_type": "MESH",
                        "primitive": "CUBE",
                        "name": name,
                        "location": location,
                        "scale": scale
                    },
                    {
                        "type": "set_shade_smooth",
                        "object": name
                    }
                ]
            }
            
            # 保存到收件箱
            filepath = save_json_to_inbox(actions_plan, "cube")
            
            return {
                "success": True,
                "message": f"成功创建立方体动作计划: {name}",
                "filepath": filepath,
                "json_type": "blender_actions",
                "action_count": 2
            }
            
        except Exception as e:
            return {
                "success": False,
                "message": f"创建立方体动作计划时发生错误: {str(e)}",
                "filepath": None
            }

    @staticmethod
    def get_system_status() -> Dict[str, Any]:
        """
        获取系统状态信息
        
        Returns:
            系统状态字典
        """
        try:
            # 统计文件数量
            inbox_count = len([f for f in os.listdir(BVTK_INBOX_DIR) if f.endswith('.json')]) if os.path.exists(BVTK_INBOX_DIR) else 0
            processed_count = len([f for f in os.listdir(BVTK_PROCESSED_DIR) if f.endswith('.json')]) if os.path.exists(BVTK_PROCESSED_DIR) else 0
            failed_count = len([f for f in os.listdir(BVTK_FAILED_DIR) if f.endswith('.json')]) if os.path.exists(BVTK_FAILED_DIR) else 0
            
            return {
                "success": True,
                "message": "系统状态正常",
                "status": {
                    "project_root": PROJECT_ROOT,
                    "inbox_files": inbox_count,
                    "processed_files": processed_count,
                    "failed_files": failed_count,
                    "total_files": inbox_count + processed_count + failed_count
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "message": f"获取系统状态时发生错误: {str(e)}",
                "status": None
            }
