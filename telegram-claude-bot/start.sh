#!/bin/bash
# Telegram Claude Bot Starter
# Starts both the bridge and command processor

cd /Users/colinyu/Projects/telegram-claude-bot

# Kill any existing processes
pkill -f "bridge.py" 2>/dev/null
pkill -f "command_processor.py" 2>/dev/null
sleep 1

echo "Starting Telegram Claude Code Bridge..."

# Unset proxy (Telegram API doesn't work well with proxies)
unset http_proxy
unset https_proxy
unset HTTP_PROXY
unset HTTPS_PROXY
unset ALL_PROXY

# Start command processor in background
echo "Starting command processor..."
nohup python3 command_processor.py > /tmp/command_processor.log 2>&1 &
PROCESSOR_PID=$!

# Start bridge in background
echo "Starting bridge..."
nohup python3 -u bridge.py > /tmp/bridge.log 2>&1 &
BRIDGE_PID=$!

echo ""
echo "✅ Bridge started!"
echo "   - Command Processor PID: $PROCESSOR_PID"
echo "   - Bridge PID: $BRIDGE_PID"
echo ""
echo "Logs:"
echo "   - Processor: /tmp/command_processor.log"
echo "   - Bridge: /tmp/bridge.log"
echo ""
echo "To stop: pkill -f 'bridge.py'; pkill -f 'command_processor.py'"
