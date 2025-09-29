# Open WebUI Action Functions 解决方案总结

## 问题描述

用户希望利用 Open WebUI 的 Action Function 功能，对 AI 输出信息中的 JSON 文件进行提取、保存，并移动到特定文件夹，然后自动识别 JSON 文件并利用对应的函数导入到 Blender 中。

## 解决方案

我们创建了一个完整的 Open WebUI Action Functions 系统，实现了以下功能：

### 1. 核心功能

- **JSON 提取**: 从 AI 输出文本中智能提取 JSON 数据
- **类型检测**: 自动识别 BVtkNodes 节点树 JSON 和 Blender 动作计划 JSON
- **文件管理**: 自动保存到收件箱，处理完成后移动到相应目录
- **Blender 集成**: 直接导入到 Blender 中，支持节点树和动作执行
- **批量处理**: 支持批量处理收件箱中的所有文件

### 2. 技术架构

```
AI 输出文本
    ↓
extract_bvtk_json (Action Function)
    ↓
JSON 检测和类型识别
    ↓
保存到收件箱 (bvtk-bridge/inbox/)
    ↓
import_bvtk_json_to_blender (Action Function)
    ↓
导入到 Blender 或移动到处理目录
```

### 3. 文件结构

```
connect/open-webui-actions/
├── openwebui_functions.py    # 主要的 Action Functions 实现
├── actions.json              # Action Functions 定义文件
├── bvtk_json_extractor.py    # 核心 JSON 处理模块
├── test_openwebui_functions.py  # 测试脚本
├── setup.py                  # 环境设置脚本
├── deploy.sh                 # 快速部署脚本
├── DEPLOYMENT_GUIDE.md       # 部署指南
└── SOLUTION_SUMMARY.md       # 本总结文档
```

## 实现的 Action Functions

### 1. extract_bvtk_json

- **功能**: 从 AI 输出文本中提取 JSON 数据并保存到收件箱
- **参数**: `text` (包含 JSON 的文本), `filename_prefix` (文件名前缀)
- **返回**: 操作结果，包含文件路径、JSON 类型、节点/动作数量等

### 2. import_bvtk_json_to_blender

- **功能**: 将 JSON 文件导入到 Blender 中
- **参数**: `filepath` (JSON 文件路径)
- **返回**: 导入结果，包含成功状态、节点/连接数量等

### 3. list_inbox_files

- **功能**: 列出收件箱中的所有 JSON 文件
- **参数**: 无
- **返回**: 文件列表，包含文件名、大小、修改时间等

### 4. process_all_inbox_files

- **功能**: 批量处理收件箱中的所有文件
- **参数**: 无
- **返回**: 处理结果，包含成功/失败数量、详细结果等

### 5. create_bvtk_sphere

- **功能**: 创建球体的 BVtkNodes 配置
- **参数**: `radius` (半径), `center` (中心坐标), `resolution` (分辨率)
- **返回**: 生成的配置文件路径和节点信息

### 6. create_blender_cube

- **功能**: 创建立方体的 Blender 动作计划
- **参数**: `name` (名称), `location` (位置), `scale` (缩放)
- **返回**: 生成的动作计划文件路径和动作信息

### 7. get_system_status

- **功能**: 获取系统状态信息
- **参数**: 无
- **返回**: 系统状态，包含文件统计、目录信息等

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

1. **AI 生成 JSON**: 用户请求 AI 生成 BVtkNodes 或 Blender 配置
2. **自动提取**: 系统自动检测 AI 输出中的 JSON 数据
3. **保存到收件箱**: JSON 文件保存到 `bvtk-bridge/inbox/` 目录
4. **导入 Blender**: 通过 Action Function 将 JSON 导入到 Blender
5. **文件管理**: 处理完成后移动到 `processed/` 或 `failed/` 目录

## 部署步骤

### 1. 快速部署

```bash
# 设置环境变量
export OPENWEBUI_DIR="/path/to/open-webui"
export CONNECT_PROJECT_ROOT="/home/kazure/Developments/simulation/final"

# 运行部署脚本
cd /home/kazure/Developments/simulation/final/connect/open-webui-actions
./deploy.sh
```

### 2. 手动部署

```bash
# 复制文件
cp openwebui_functions.py $OPENWEBUI_DIR/functions/
cp actions.json $OPENWEBUI_DIR/functions/

# 启动 Open WebUI
cd $OPENWEBUI_DIR
python -m openwebui.serve --host 0.0.0.0 --port 8080
```

### 3. 在 Open WebUI 中启用

1. 打开管理界面
2. 进入 Settings > Functions
3. 启用所有 BVtkNodes 相关的 Action Functions

## 测试验证

运行测试脚本验证所有功能：

```bash
cd /home/kazure/Developments/simulation/final/connect/open-webui-actions
python3 test_openwebui_functions.py
```

测试结果：✅ 7/7 通过

## 优势特性

### 1. 智能 JSON 提取

- 支持多种 JSON 格式（代码块、内联 JSON）
- 自动检测和验证 JSON 有效性
- 支持 BVtkNodes 和 Blender 动作两种格式

### 2. 自动化工作流

- 无需手动干预，AI 输出自动处理
- 文件自动分类和管理
- 错误处理和日志记录

### 3. 灵活配置

- 支持自定义文件名前缀
- 可配置的目录结构
- 环境变量支持

### 4. 监控和调试

- 系统状态监控
- 详细的错误信息
- 文件处理统计

### 5. 扩展性

- 易于添加新的 Action Functions
- 支持自定义 JSON 格式
- 模块化设计

## 使用示例

### 在 Open WebUI 中使用

```
用户: 请生成一个球体的 BVtkNodes 配置

AI: 我来为您生成球体的 BVtkNodes 配置...

[AI 生成包含 JSON 的响应]

[系统自动调用 extract_bvtk_json 函数]
[JSON 保存到收件箱]
[用户可以选择导入到 Blender]
```

### 直接调用 Action Functions

```
用户: 请列出收件箱中的所有文件

AI: [调用 list_inbox_files 函数并显示结果]
```

## 故障排除

### 常见问题

1. **"No Function class found in the module"** - 确保文件包含 Function 类
2. **JSON 提取失败** - 检查 AI 输出格式
3. **Blender 导入失败** - 确保 Blender 运行且插件已启用

### 调试方法

1. 查看 Open WebUI 日志
2. 检查 `bvtk-bridge/failed/` 目录
3. 运行测试脚本验证功能

## 总结

这个解决方案完全满足了用户的需求：

1. ✅ **JSON 提取**: 从 AI 输出中自动提取 JSON 数据
2. ✅ **文件保存**: 自动保存到指定文件夹
3. ✅ **文件移动**: 处理完成后移动到相应目录
4. ✅ **Blender 集成**: 自动识别并导入到 Blender
5. ✅ **Open WebUI 集成**: 通过 Action Functions 实现

系统具有高度的自动化、灵活性和可扩展性，能够处理各种 JSON 格式，并提供完整的监控和调试功能。
