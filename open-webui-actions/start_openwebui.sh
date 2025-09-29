#!/bin/bash
# Open WebUI 启动脚本（包含 BVtkNodes Action Functions）

export CONNECT_PROJECT_ROOT=/home/kazure/Developments/simulation/final
export BVTK_INBOX_DIR=/home/kazure/Developments/simulation/final/connect/bvtk-bridge/inbox

# 启动 Open WebUI
cd /home/kazure/Developments/simulation/final/open-webui
python -m openwebui.serve --host 0.0.0.0 --port 8080
