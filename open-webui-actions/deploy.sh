#!/bin/bash
# Open WebUI Action Functions 快速部署脚本

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 打印带颜色的消息
print_message() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 检查 Open WebUI 目录
check_openwebui_dir() {
    if [ -z "$OPENWEBUI_DIR" ]; then
        print_error "请设置 OPENWEBUI_DIR 环境变量"
        echo "例如: export OPENWEBUI_DIR=/path/to/open-webui"
        exit 1
    fi
    
    if [ ! -d "$OPENWEBUI_DIR" ]; then
        print_error "Open WebUI 目录不存在: $OPENWEBUI_DIR"
        exit 1
    fi
    
    if [ ! -d "$OPENWEBUI_DIR/functions" ]; then
        print_warning "functions 目录不存在，正在创建..."
        mkdir -p "$OPENWEBUI_DIR/functions"
    fi
}

# 复制文件
copy_files() {
    print_message "复制 Action Functions 文件..."
    
    # 复制主要文件
    cp openwebui_functions.py "$OPENWEBUI_DIR/functions/"
    cp actions.json "$OPENWEBUI_DIR/functions/"
    
    print_message "文件复制完成"
}

# 设置权限
set_permissions() {
    print_message "设置文件权限..."
    
    chmod +x "$OPENWEBUI_DIR/functions/openwebui_functions.py"
    chmod 644 "$OPENWEBUI_DIR/functions/actions.json"
    
    print_message "权限设置完成"
}

# 验证部署
verify_deployment() {
    print_message "验证部署..."
    
    if [ -f "$OPENWEBUI_DIR/functions/openwebui_functions.py" ]; then
        print_message "✓ openwebui_functions.py 已部署"
    else
        print_error "✗ openwebui_functions.py 部署失败"
        exit 1
    fi
    
    if [ -f "$OPENWEBUI_DIR/functions/actions.json" ]; then
        print_message "✓ actions.json 已部署"
    else
        print_error "✗ actions.json 部署失败"
        exit 1
    fi
    
    # 检查 Python 语法
    if python3 -m py_compile "$OPENWEBUI_DIR/functions/openwebui_functions.py" 2>/dev/null; then
        print_message "✓ Python 语法检查通过"
    else
        print_error "✗ Python 语法检查失败"
        exit 1
    fi
}

# 运行测试
run_tests() {
    print_message "运行测试..."
    
    if python3 test_openwebui_functions.py; then
        print_message "✓ 所有测试通过"
    else
        print_warning "⚠ 部分测试失败，请检查错误信息"
    fi
}

# 显示下一步
show_next_steps() {
    echo
    print_message "部署完成！"
    echo
    echo "下一步："
    echo "1. 启动 Open WebUI:"
    echo "   cd $OPENWEBUI_DIR"
    echo "   python -m openwebui.serve --host 0.0.0.0 --port 8080"
    echo
    echo "2. 在 Open WebUI 管理界面中启用 Action Functions:"
    echo "   - 进入 Settings > Functions"
    echo "   - 启用所有 BVtkNodes 相关的 Action Functions"
    echo
    echo "3. 测试功能:"
    echo "   - 在对话中请求生成 BVtkNodes 配置"
    echo "   - 系统会自动提取并保存 JSON 文件"
    echo
    echo "4. 查看收件箱文件:"
    echo "   ls -la $CONNECT_PROJECT_ROOT/connect/bvtk-bridge/inbox/"
    echo
}

# 主函数
main() {
    echo "Open WebUI Action Functions 部署脚本"
    echo "====================================="
    echo
    
    # 检查环境变量
    if [ -z "$CONNECT_PROJECT_ROOT" ]; then
        export CONNECT_PROJECT_ROOT="/home/kazure/Developments/simulation/final"
        print_warning "使用默认项目根目录: $CONNECT_PROJECT_ROOT"
    fi
    
    # 检查 Open WebUI 目录
    check_openwebui_dir
    
    # 复制文件
    copy_files
    
    # 设置权限
    set_permissions
    
    # 验证部署
    verify_deployment
    
    # 运行测试
    run_tests
    
    # 显示下一步
    show_next_steps
}

# 运行主函数
main "$@"
