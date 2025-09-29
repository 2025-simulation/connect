### 项目目的

利用 open-webui 的 function 功能 pipe 函数，捕获终端调用 graphrag 的输出，然后检测其中的 JSON 代码，保存为文件，放在 connect/bvtk-bridge/inbox 下

1. 捕获输出，然后利用 open-webui 的界面显示 AI 的回答
2. 检测 JSON 代码，保存为文件，放在 connect/bvtk-bridge/inbox 下

### 使用步骤（最简）

1. 在 Open-WebUI 中导入管道脚本：

- 选择模型/函数 → 导入 Python Pipe → 选择 `connect/graphrag/advanced-streaming-pipe.py`
- 或导入 `connect/graphrag/to_bvtk_json_pipe.py`（带 LLM 兜底与更强 JSON 处理）

2. 在阀门配置中（可选）检查：

- `GRAPHRAG_PATH`: 本地 graphrag Python 可执行路径
- `GRAPHRAG_CWD`: graphrag 项目工作目录
- `RAG_ROOT`: graphrag 数据目录（如 `./ragtest`）
- `INBOX_DIR`: JSON 落盘目录（默认 `connect/bvtk-bridge/inbox`）

3. 在聊天中直接提问：

- 勾选流式显示可实时看到输出；脚本会自动尝试从输出中抽取 JSON 并保存到 `INBOX_DIR`
- 非流式也会在返回文本中附加 `[Saved JSON to: /path/xxx.json]` 提示

4. Blender 侧（可选）：

- 启用自动加载插件后会监控 `inbox/` 并导入动作 JSON（参考 `connect/README.org` 的一键配置）
