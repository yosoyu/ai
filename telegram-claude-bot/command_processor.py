#!/usr/bin/env python3
"""
Command Processor for Telegram → Claude Code Bridge
Automatically processes pending commands from the queue.
Supports confirmation dialogs for dangerous operations.
"""

import json
import os
import subprocess
import time
import re
from datetime import datetime
from anthropic import Anthropic

QUEUE_FILE = "/tmp/claude_commands/queue.json"

# Initialize Anthropic client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Dangerous command patterns that require confirmation
DANGEROUS_PATTERNS = [
    r'\brm\s+-rf\b',
    r'\brm\s+.*\*',
    r'\bgit\s+push\s+.*--force',
    r'\bgit\s+reset\s+--hard',
    r'\bgit\s+clean\s+-fd',
    r'\bdd\s+if=',
    r'\bmkfs\b',
    r'\b:\(\)\{\s*:\|:&\s*\};\s*:',  # fork bomb
    r'\bchmod\s+777',
    r'\bsudo\s+',
    r'\biptables\b',
    r'\bkill\s+-9\b',
    r'\bpkill\b',
    r'\btruncate\b',
    r'\bshred\b',
    r'\b>.*\b',  # file overwrites
]

def load_queue():
    try:
        with open(QUEUE_FILE, 'r') as f:
            return json.load(f)
    except:
        return {"commands": [], "responses": {}, "confirmations": {}}

def save_queue(queue):
    with open(QUEUE_FILE, 'w') as f:
        json.dump(queue, f, indent=2)

def is_dangerous_command(command: str) -> tuple:
    """Check if command is potentially dangerous. Returns (is_dangerous, reason)."""
    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return True, f"Matches dangerous pattern: {pattern}"
    return False, None

def process_claude_command(cmd: dict, queue: dict) -> tuple:
    """Process a Claude command. Returns (status, result)."""
    content = cmd["content"]
    conversation_history = cmd.get("conversation", [])

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            system="""You are a helpful assistant processing commands from a Telegram bot.
Be concise but thorough.
If you need to perform a potentially dangerous operation, clearly state what you're about to do and ask for confirmation.
Use 'CONFIRMATION_REQUIRED:' prefix if you need user confirmation before proceeding.""",
            messages=conversation_history + [{"role": "user", "content": content}]
        )
        result = response.content[0].text

        # Check if Claude is asking for confirmation
        if "CONFIRMATION_REQUIRED:" in result or needs_user_confirmation(result):
            return "awaiting_confirmation", result

        return "completed", result
    except Exception as e:
        return "completed", f"Error calling Claude: {e}"

def needs_user_confirmation(response: str) -> bool:
    """Detect if the response indicates a need for user confirmation."""
    confirmation_phrases = [
        "do you want me to",
        "should i proceed",
        "confirm",
        "would you like me to",
        "may i",
        "can i delete",
        "are you sure",
        "proceed with",
        "continue?",
    ]
    response_lower = response.lower()
    return any(phrase in response_lower for phrase in confirmation_phrases)

def process_shell_command(cmd: dict, queue: dict) -> tuple:
    """Run a shell command. Returns (status, result)."""
    command = cmd["content"]

    # Check if command is dangerous
    is_dangerous, reason = is_dangerous_command(command)
    if is_dangerous:
        return "awaiting_confirmation", f"⚠️ Dangerous command detected!\n\nCommand: `{command}`\nReason: {reason}\n\nDo you want to proceed? Reply /confirm or /cancel"

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        output = result.stdout
        if result.stderr:
            output += f"\nStderr: {result.stderr}"
        if result.returncode != 0:
            output += f"\nExit code: {result.returncode}"
        return "completed", output if output else "(no output)"
    except subprocess.TimeoutExpired:
        return "completed", "Command timed out after 30 seconds"
    except Exception as e:
        return "completed", f"Error: {e}"

def process_read_file(filepath: str) -> tuple:
    """Read a file. Returns (status, result)."""
    try:
        allowed_dirs = ["/Users/colinyu/Projects", "/Users/colinyu/.claude", "/tmp"]
        resolved = os.path.realpath(filepath)

        allowed = any(resolved.startswith(d) for d in allowed_dirs)
        if not allowed:
            return "completed", f"Access denied: Can only read from {allowed_dirs}"

        with open(filepath, 'r') as f:
            content = f.read()
        if len(content) > 4000:
            content = content[:4000] + "\n... (truncated)"
        return "completed", content
    except FileNotFoundError:
        return "completed", f"File not found: {filepath}"
    except Exception as e:
        return "completed", f"Error reading file: {e}"

def process_confirmation_response(cmd: dict, queue: dict) -> tuple:
    """Process a user's confirmation response."""
    user_response = cmd["content"].lower().strip()
    original_cmd_id = cmd.get("original_cmd_id")

    if not original_cmd_id:
        return "completed", "Error: No original command found for confirmation"

    # Find the original command
    original_cmd = None
    for c in queue["commands"]:
        if c["id"] == original_cmd_id:
            original_cmd = c
            break

    if not original_cmd:
        return "completed", f"Error: Original command {original_cmd_id} not found"

    if user_response in ["confirm", "yes", "y", "/confirm", "proceed"]:
        # User confirmed - execute the dangerous command
        if original_cmd["type"] == "shell_command":
            try:
                result = subprocess.run(
                    original_cmd["content"],
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                output = result.stdout
                if result.stderr:
                    output += f"\nStderr: {result.stderr}"
                return "completed", output if output else "(no output)"
            except Exception as e:
                return "completed", f"Error: {e}"
        else:
            return "completed", "Confirmation received, but no action defined for this command type"

    elif user_response in ["cancel", "no", "n", "/cancel", "deny", "/deny"]:
        return "completed", "❌ Command cancelled by user"
    else:
        return "awaiting_confirmation", f"Unknown response. Please reply with /confirm or /cancel"

def process_commands():
    """Process all pending commands."""
    queue = load_queue()
    pending = [c for c in queue["commands"] if c["status"] == "pending"]

    if not pending:
        return 0

    processed = 0
    for cmd in pending:
        cmd_type = cmd["type"]
        cmd_id = cmd["id"]

        print(f"[{datetime.now().strftime('%H:%M:%S')}] Processing {cmd_id}: {cmd_type}...")

        status = "completed"
        result = None

        if cmd_type == "claude_command":
            status, result = process_claude_command(cmd, queue)
        elif cmd_type == "shell_command":
            status, result = process_shell_command(cmd, queue)
        elif cmd_type == "read_file":
            status, result = process_read_file(cmd["content"])
        elif cmd_type == "confirmation_response":
            status, result = process_confirmation_response(cmd, queue)
        else:
            result = f"Unknown command type: {cmd_type}"

        # Update command status
        for c in queue["commands"]:
            if c["id"] == cmd_id:
                c["status"] = status
                if status == "awaiting_confirmation":
                    c["confirmation_message"] = result
                break

        # Add response if completed
        if status == "completed":
            queue["responses"][cmd_id] = {
                "result": result,
                "completed_at": datetime.now().isoformat()
            }
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Completed {cmd_id}")
        else:
            # For awaiting_confirmation, still add a response so bridge can notify user
            queue["responses"][cmd_id] = {
                "result": result,
                "requires_confirmation": True,
                "completed_at": datetime.now().isoformat()
            }
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Awaiting confirmation for {cmd_id}")

        processed += 1

    save_queue(queue)
    return processed

def main():
    print("=" * 50)
    print("Command Processor Started")
    print("=" * 50)
    print(f"Watching: {QUEUE_FILE}")
    print("Press Ctrl+C to stop")
    print("-" * 50)

    while True:
        try:
            processed = process_commands()
            if processed > 0:
                print(f"Processed {processed} command(s)")
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()

        time.sleep(1)

if __name__ == "__main__":
    main()
