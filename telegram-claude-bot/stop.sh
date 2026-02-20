#!/bin/bash
# Stop Telegram Claude Bot

echo "Stopping Telegram Claude Code Bridge..."

pkill -f "bridge.py" 2>/dev/null
pkill -f "command_processor.py" 2>/dev/null

echo "✅ Stopped"
