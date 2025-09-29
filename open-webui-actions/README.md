# Open WebUI Action Functions for BVtkNodes

这个模块提供了 Open WebUI 的 Action Functions，用于从 AI 输出中提取 BVtkNodes JSON 数据并自动导入到 Blender 中。

## 功能特性

- **JSON 提取**: 从 AI 输出文本中智能提取 JSON 数据
- **类型检测**: 自动识别 BVtkNodes 节点树 JSON 和 Blender 动作计划 JSON
- **文件管理**: 自动保存到收件箱，处理完成后移动到相应目录
- **Blender 集成**: 直接导入到 Blender 中，支持节点树和动作执行
- **批量处理**: 支持批量处理收件箱中的所有文件

## 安装配置

### 1. 环境准备

确保已安装以下依赖：

```bash
# 在 Blender 环境中
pip install bpy
```

### 2. Open WebUI 配置

1. 将 `actions.json` 和 `action_functions.py` 复制到 Open WebUI 的 actions 目录
2. 在 Open WebUI 管理界面中启用这些 Action Functions

### 3. 目录结构

```
connect/
├── open-webui-actions/
│   ├── actions.json              # Action Functions 定义
│   ├── action_functions.py       # Action Functions 实现
│   ├── bvtk_json_extractor.py    # 核心处理模块
│   └── README.md                 # 说明文档
└── bvtk-bridge/
    ├── inbox/                    # 收件箱目录
    ├── processed/                # 已处理文件目录
    └── failed/                   # 失败文件目录
```

## Action Functions 说明

### 1. extract_bvtk_json

从 AI 输出文本中提取 JSON 数据并保存到收件箱。

**参数:**

- `text` (string): 包含 JSON 的文本
- `filename_prefix` (string, 可选): 文件名前缀，默认为 "bvtk"

**返回:**

```json
{
  "success": true,
  "message": "成功提取并保存 bvtk_tree JSON 到收件箱",
  "filepath": "/path/to/saved/file.json",
  "json_type": "bvtk_tree",
  "node_count": 5,
  "action_count": null
}
```

### 2. import_bvtk_json_to_blender

将 JSON 文件导入到 Blender 中。

**参数:**

- `filepath` (string): JSON 文件的完整路径

**返回:**

```json
{
  "success": true,
  "message": "成功导入 5 个节点和 4 个连接",
  "node_count": 5,
  "link_count": 4,
  "processed_path": "/path/to/processed/file.json"
}
```

### 3. list_inbox_files

列出收件箱中的所有 JSON 文件。

**返回:**

```json
{
  "success": true,
  "files": [
    {
      "filename": "bvtk-20241201-143022.json",
      "filepath": "/path/to/file.json",
      "size": 1024,
      "modified": "2024-12-01T14:30:22"
    }
  ],
  "count": 1
}
```

### 4. process_all_inbox_files

批量处理收件箱中的所有文件。

**返回:**

```json
{
  "success": true,
  "message": "处理完成: 3 成功, 1 失败",
  "processed_count": 3,
  "failed_count": 1,
  "results": [...]
}
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
    },
    {
      "type": "add_modifier",
      "object": "MyCube",
      "modifier": "SUBSURF",
      "levels": 2
    }
  ]
}
```

## 使用示例

### 在 Open WebUI 中使用

1. **提取 JSON**: 当 AI 输出包含 JSON 数据时，调用 `extract_bvtk_json` 函数
2. **导入 Blender**: 使用 `import_bvtk_json_to_blender` 将 JSON 导入到 Blender
3. **批量处理**: 使用 `process_all_inbox_files` 处理所有待处理文件

### 在 Blender 中使用

1. 确保 BVtkNodes 插件已安装并启用
2. 在节点编辑器中切换到 BVtkNodes 节点树
3. 通过 Action Functions 导入 JSON 数据

## 错误处理

- 无效的 JSON 数据会被移动到 `failed` 目录
- 错误信息会保存到对应的 `.error.txt` 文件中
- 处理成功的文件会移动到 `processed` 目录

## 环境变量

- `CONNECT_PROJECT_ROOT`: 项目根目录路径
- `BVTK_INBOX_DIR`: 收件箱目录路径（可选）

## 注意事项

1. 确保 Blender 正在运行且 BVtkNodes 插件已启用
2. 在节点编辑器中执行导入操作
3. 大型节点树可能需要较长的处理时间
4. 建议定期清理 `processed` 和 `failed` 目录

## 故障排除

### 常见问题

1. **"请在节点编辑器中执行此操作"**

   - 确保在 Blender 的节点编辑器中
   - 切换到 BVtkNodes 节点树类型

2. **"未在文本中找到有效的 JSON 数据"**

   - 检查文本中是否包含有效的 JSON
   - 确保 JSON 格式正确

3. **"不支持的 JSON 类型"**
   - 检查 JSON 是否包含 `nodes`/`links` 或 `actions` 字段
   - 确保 JSON 结构符合预期格式

### 调试方法

1. 查看 `failed` 目录中的错误文件
2. 检查 Blender 控制台输出
3. 使用 `list_inbox_files` 查看文件状态
