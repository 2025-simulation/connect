
# Open WebUI 集成指南

## 1. 安装 Action Functions

将以下文件复制到 Open WebUI 的 actions 目录：

```
open-webui-actions/
├── actions.json
├── action_functions.py
└── bvtk_json_extractor.py
```

## 2. 配置 Open WebUI

在 Open WebUI 管理界面中：

1. 进入 Settings > Functions
2. 启用以下 Action Functions：
   - `extract_bvtk_json`
   - `import_bvtk_json_to_blender`
   - `list_inbox_files`
   - `process_all_inbox_files`

## 3. 在对话中使用

### 方法 1: 直接调用 Action Functions

在对话中，AI 可以自动调用这些函数：

```
用户: 请生成一个球体的 BVtkNodes 配置

AI: 我来为您生成球体的 BVtkNodes 配置...

[AI 生成 JSON 配置]

[自动调用 extract_bvtk_json 保存到收件箱]
[自动调用 import_bvtk_json_to_blender 导入到 Blender]
```

### 方法 2: 手动调用

用户也可以手动调用这些函数：

```
用户: 请处理收件箱中的所有文件

AI: [调用 process_all_inbox_files 函数]
```

## 4. 工作流程

1. **AI 生成 JSON**: AI 根据用户需求生成 BVtkNodes 或 Blender 动作 JSON
2. **自动提取**: 系统自动检测并提取 JSON 数据
3. **保存到收件箱**: JSON 文件保存到 `bvtk-bridge/inbox/` 目录
4. **导入 Blender**: 自动将 JSON 导入到 Blender 中
5. **文件管理**: 处理完成后移动到 `processed/` 或 `failed/` 目录

## 5. 监控和调试

- 使用 `list_inbox_files` 查看待处理文件
- 检查 `bvtk-bridge/failed/` 目录中的错误文件
- 查看 Blender 控制台输出获取详细错误信息

## 6. 自定义配置

可以通过环境变量自定义路径：

```bash
export CONNECT_PROJECT_ROOT="/path/to/your/project"
export BVTK_INBOX_DIR="/path/to/custom/inbox"
```
