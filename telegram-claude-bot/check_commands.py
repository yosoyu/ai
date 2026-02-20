#!/usr/bin/env python3
"""
Command Processor for Claude Code
Run this to see pending commands from Telegram.

Usage:
    python3 check_commands.py              # List pending commands
    python3 check_commands.py <id> <result> # Add response for command
"""

import json
import sys
from datetime import datetime

QUEUE_FILE = "/tmp/claude_commands/queue.json"

def load_queue():
    try:
        with open(QUEUE_FILE, 'r') as f:
            return json.load(f)
    except:
        return {"commands": [], "responses": {}}

def save_queue(queue):
    with open(QUEUE_FILE, 'w') as f:
        json.dump(queue, f, indent=2)

def list_pending():
    queue = load_queue()
    pending = [c for c in queue["commands"] if c["status"] == "pending"]

    if not pending:
        print("No pending commands.")
        return

    print(f"Found {len(pending)} pending command(s):\n")
    for cmd in pending:
        print(f"ID: {cmd['id']}")
        print(f"Type: {cmd['type']}")
        print(f"Content: {cmd['content']}")
        print(f"Time: {cmd['timestamp']}")
        print("-" * 40)

def add_response(cmd_id, result_file):
    queue = load_queue()

    # Read result from file or direct input
    if result_file == "-":
        result = sys.stdin.read()
    elif result_file.startswith('"'):
        result = result_file.strip('"')
    else:
        try:
            with open(result_file, 'r') as f:
                result = f.read()
        except:
            result = result_file

    queue["responses"][cmd_id] = {
        "result": result,
        "completed_at": datetime.now().isoformat()
    }

    save_queue(queue)
    print(f"Response added for command {cmd_id}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        list_pending()
    elif len(sys.argv) >= 3:
        add_response(sys.argv[1], sys.argv[2])
    else:
        print("Usage:")
        print("  python3 check_commands.py                    # List pending")
        print("  python3 check_commands.py <id> <result_file> # Add response")
