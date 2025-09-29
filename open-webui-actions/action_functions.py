"""
Open WebUI Action Functions Implementation
Open WebUI Action Functions 实现文件
"""

import sys
import os
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = os.environ.get("CONNECT_PROJECT_ROOT", "/home/kazure/Developments/simulation/final")
sys.path.insert(0, os.path.join(project_root, "connect", "open-webui-actions"))

# 导入 BVtkNodes JSON 处理模块
from bvtk_json_extractor import (
    extract_and_save_bvtk_json,
    import_bvtk_json_to_blender,
    list_inbox_files,
    process_all_inbox_files
)


class Function:
    """Open WebUI Action Functions 基类"""
    
    @staticmethod
    def extract_bvtk_json(text: str, filename_prefix: str = "bvtk") -> dict:
        """
        Action Function: 从文本中提取并保存 BVtkNodes JSON
        
        Args:
            text: 包含 JSON 的文本
            filename_prefix: 文件名前缀
            
        Returns:
            操作结果字典
        """
        return extract_and_save_bvtk_json(text, filename_prefix)

    @staticmethod
    def import_bvtk_json_to_blender_action(filepath: str) -> dict:
        """
        Action Function: 将 BVtkNodes JSON 导入到 Blender
        
        Args:
            filepath: JSON 文件路径
            
        Returns:
            操作结果字典
        """
        return import_bvtk_json_to_blender(filepath)

    @staticmethod
    def list_inbox_files_action() -> dict:
        """
        Action Function: 列出收件箱中的文件
        
        Returns:
            文件列表字典
        """
        return list_inbox_files()

    @staticmethod
    def process_all_inbox_files_action() -> dict:
        """
        Action Function: 批量处理收件箱中的所有文件
        
        Returns:
            处理结果字典
        """
        return process_all_inbox_files()


# 为了向后兼容，也提供函数形式的接口
def extract_bvtk_json(text: str, filename_prefix: str = "bvtk") -> dict:
    """从文本中提取并保存 BVtkNodes JSON"""
    return extract_and_save_bvtk_json(text, filename_prefix)


def import_bvtk_json_to_blender_action(filepath: str) -> dict:
    """将 BVtkNodes JSON 导入到 Blender"""
    return import_bvtk_json_to_blender(filepath)


def list_inbox_files_action() -> dict:
    """列出收件箱中的文件"""
    return list_inbox_files()


def process_all_inbox_files_action() -> dict:
    """批量处理收件箱中的所有文件"""
    return process_all_inbox_files()
