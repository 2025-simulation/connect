"""
Open WebUI Action Functions for BVtkNodes
符合 Open WebUI 标准的 Action Functions 实现
"""

import sys
import os
import json
from pathlib import Path
from typing import Dict, Any, List, Optional

# 添加项目根目录到 Python 路径
project_root = os.environ.get("CONNECT_PROJECT_ROOT", "/home/kazure/Developments/simulation/final")
sys.path.insert(0, os.path.join(project_root, "connect", "open-webui-actions"))

# 导入 BVtkNodes JSON 处理模块
from bvtk_json_extractor import (
    extract_json_from_text,
    detect_bvtk_json_type,
    save_json_to_inbox,
    import_bvtk_json_to_blender,
    list_inbox_files,
    process_all_inbox_files
)


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
            return import_bvtk_json_to_blender(filepath)
        except Exception as e:
            return {
                "success": False,
                "message": f"导入 JSON 时发生错误: {str(e)}",
                "filepath": filepath
            }

    @staticmethod
    def list_inbox_files() -> Dict[str, Any]:
        """
        列出收件箱中的所有 JSON 文件
        
        Returns:
            文件列表字典
        """
        try:
            result = list_inbox_files()
            if result.get("success"):
                return result
            else:
                return {
                    "success": False,
                    "message": result.get("message", "未知错误"),
                    "files": []
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
            return process_all_inbox_files()
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
            project_root = os.environ.get("CONNECT_PROJECT_ROOT", "/home/kazure/Developments/simulation/final")
            inbox_dir = os.path.join(project_root, "connect", "bvtk-bridge", "inbox")
            processed_dir = os.path.join(project_root, "connect", "bvtk-bridge", "processed")
            failed_dir = os.path.join(project_root, "connect", "bvtk-bridge", "failed")
            
            # 统计文件数量
            inbox_count = len([f for f in os.listdir(inbox_dir) if f.endswith('.json')]) if os.path.exists(inbox_dir) else 0
            processed_count = len([f for f in os.listdir(processed_dir) if f.endswith('.json')]) if os.path.exists(processed_dir) else 0
            failed_count = len([f for f in os.listdir(failed_dir) if f.endswith('.json')]) if os.path.exists(failed_dir) else 0
            
            return {
                "success": True,
                "message": "系统状态正常",
                "status": {
                    "project_root": project_root,
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
