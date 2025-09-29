# Open WebUI Action Functions 部署指南

## 概述

本指南将帮助您将 BVtkNodes JSON 处理功能部署到 Open WebUI 中，实现从 AI 输出中自动提取 JSON 数据并导入到 Blender 的完整工作流程。

## 文件结构

```
connect/open-webui-actions/
├── openwebui_functions.py    # 主要的 Action Functions 实现
├── actions.json              # Action Functions 定义文件
├── bvtk_json_extractor.py    # 核心 JSON 处理模块
├── test_openwebui_functions.py  # 测试脚本
├── setup.py                  # 环境设置脚本
└── DEPLOYMENT_GUIDE.md       # 本部署指南
```

## 部署步骤

### 1. 环境准备

确保已安装以下依赖：

```bash
# Python 依赖
pip install pydantic pathlib

# 如果要在 Blender 中使用，需要安装 bpy
# 注意：bpy 只在 Blender 环境中可用
```

### 2. 复制文件到 Open WebUI

将以下文件复制到 Open WebUI 的 functions 目录：

```bash
# 假设 Open WebUI 安装在 /path/to/open-webui
cp openwebui_functions.py /path/to/open-webui/functions/
cp actions.json /path/to/open-webui/functions/
```

### 3. 配置环境变量

设置必要的环境变量：

```bash
export CONNECT_PROJECT_ROOT="/home/kazure/Developments/simulation/final"
export BVTK_INBOX_DIR="/home/kazure/Developments/simulation/final/connect/bvtk-bridge/inbox"
```

### 4. 启动 Open WebUI

```bash
cd /path/to/open-webui
python -m openwebui.serve --host 0.0.0.0 --port 8080
```

### 5. 在 Open WebUI 中启用 Action Functions

1. 打开 Open WebUI 管理界面
2. 进入 Settings > Functions
3. 启用以下 Action Functions：
   - `extract_bvtk_json`
   - `import_bvtk_json_to_blender`
   - `list_inbox_files`
   - `process_all_inbox_files`
   - `create_bvtk_sphere`
   - `create_blender_cube`
   - `get_system_status`

## 使用方法

### 1. 从 AI 输出提取 JSON

在对话中，AI 可以自动调用 `extract_bvtk_json` 函数：

```
用户: 请生成一个球体的 BVtkNodes 配置

AI: 我来为您生成球体的 BVtkNodes 配置...

[AI 生成包含 JSON 的响应]

[系统自动调用 extract_bvtk_json 函数，将 JSON 保存到收件箱]
```

### 2. 手动调用 Action Functions

用户也可以直接调用这些函数：

```
用户: 请列出收件箱中的所有文件

AI: [调用 list_inbox_files 函数并显示结果]
```

### 3. 创建预定义配置

使用预定义的函数快速创建常用配置：

```
用户: 创建一个半径为 3 的球体

AI: [调用 create_bvtk_sphere 函数，参数 radius=3]
```

## 支持的 JSON 格式

### 1. BVtkNodes 节点树 JSON

```json
{
  "nodes": [
    {
      "bl_idname": "VTKSphereSourceType",
      "name": "vtkSphereSource",
      "location": [0, 0],
      "m_Radius": 1.0,
      "m_Center": [0, 0, 0]
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

### 2. Blender 动作计划 JSON

```json
{
  "version": 1,
  "doc": "创建基础几何体",
  "actions": [
    {
      "type": "create_object",
      "object_type": "MESH",
      "primitive": "CUBE",
      "name": "MyCube",
      "location": [0, 0, 0],
      "scale": [2, 2, 2]
    }
  ]
}
```

## 工作流程

1. **AI 生成 JSON**: AI 根据用户需求生成 BVtkNodes 或 Blender 动作 JSON
2. **自动提取**: 系统自动检测并提取 JSON 数据
3. **保存到收件箱**: JSON 文件保存到 `bvtk-bridge/inbox/` 目录
4. **导入 Blender**: 通过 `import_bvtk_json_to_blender` 函数导入到 Blender
5. **文件管理**: 处理完成后移动到 `processed/` 或 `failed/` 目录

## 监控和调试

### 1. 查看系统状态

```python
# 调用 get_system_status 函数
result = Function.get_system_status()
print(f"收件箱文件: {result['status']['inbox_files']}")
print(f"已处理文件: {result['status']['processed_files']}")
```

### 2. 列出文件

```python
# 调用 list_inbox_files 函数
result = Function.list_inbox_files()
for file_info in result['files']:
    print(f"{file_info['filename']} - {file_info['size']} bytes")
```

### 3. 批量处理

```python
# 调用 process_all_inbox_files 函数
result = Function.process_all_inbox_files()
print(f"处理结果: {result['processed_count']} 成功, {result['failed_count']} 失败")
```

## 故障排除

### 常见问题

1. **"No Function class found in the module"**

   - 确保 `openwebui_functions.py` 文件包含 `Function` 类
   - 检查文件路径是否正确

2. **"未在文本中找到有效的 JSON 数据"**

   - 检查 AI 输出是否包含有效的 JSON
   - 确保 JSON 格式正确

3. **"导入 JSON 时发生错误"**
   - 检查 Blender 是否正在运行
   - 确保 BVtkNodes 插件已安装并启用

### 调试方法

1. 查看 Open WebUI 日志
2. 检查 `bvtk-bridge/failed/` 目录中的错误文件
3. 使用测试脚本验证功能

## 测试

运行测试脚本验证所有功能：

```bash
cd /path/to/open-webui-actions
python3 test_openwebui_functions.py
```

## 扩展功能

### 添加新的 Action Functions

1. 在 `openwebui_functions.py` 中添加新的静态方法
2. 在 `actions.json` 中添加函数定义
3. 更新测试脚本

### 自定义 JSON 格式

修改 `bvtk_json_extractor.py` 中的 `detect_bvtk_json_type` 函数来支持新的 JSON 格式。

## 注意事项

1. 确保 Blender 正在运行且 BVtkNodes 插件已启用
2. 在节点编辑器中执行导入操作
3. 大型节点树可能需要较长的处理时间
4. 建议定期清理 `processed` 和 `failed` 目录

## 支持

如果遇到问题，请检查：

1. 文件权限
2. 环境变量设置
3. Open WebUI 版本兼容性
4. Python 依赖版本

## 更新日志

- v1.0.0: 初始版本，支持基本的 JSON 提取和导入功能
- v1.1.0: 添加预定义配置创建函数
- v1.2.0: 添加系统状态监控功能
