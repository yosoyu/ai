# Telegram Claude Code Bridge

Control your MacBook's Claude Code session from Telegram!

## Features

- **Chat Mode**: Chat directly with Claude AI
- **Command Mode**: Execute commands on your MacBook
- **Confirmation Dialogs**: Dangerous commands require confirmation via Telegram

## Setup

### 1. Install Dependencies

```bash
cd /Users/colinyu/Projects/telegram-claude-bot
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file with:

```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
ANTHROPIC_API_KEY=your_anthropic_api_key
```

### 3. Create Queue Directory

```bash
mkdir -p /tmp/claude_commands
```

## Usage

### Start the Bridge

```bash
./start.sh
```

This starts both:
- **Command Processor** - Processes queued commands
- **Bridge** - Handles Telegram communication

### Stop the Bridge

```bash
./stop.sh
```

Or manually:
```bash
pkill -f 'bridge.py'; pkill -f 'command_processor.py'
```

## Telegram Commands

### Chat Mode
Just type a message to chat with Claude AI directly.

### Command Mode
| Command | Description |
|---------|-------------|
| `/start` | Show welcome message |
| `/cmd <text>` | Send command to Claude |
| `/run <shell>` | Run shell command |
| `/read <file>` | Read a file |
| `/status` | Check pending commands |
| `/clear` | Clear chat history |
| `/confirm` | Approve a dangerous command |
| `/cancel` | Reject a dangerous command |

### Examples

```
/cmd list all files in my projects folder
/run ls -la ~/Projects
/read /Users/colinyu/Projects/test.py
```

## Confirmation System

Dangerous commands require confirmation:
- `rm -rf`
- `git push --force`
- `git reset --hard`
- `sudo`
- And more...

When detected, you'll receive:
```
⚠️ Confirmation Required

Command: `rm -rf /tmp/test`
Reason: Matches dangerous pattern

Reply with /confirm to proceed or /cancel to abort.
```

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌──────────────────┐
│  Telegram   │────▶│   bridge.py  │────▶│   queue.json     │
│   (Phone)   │◀────│  (Bot API)   │◀────│  (/tmp/...)      │
└─────────────┘     └──────────────┘     └────────┬─────────┘
                                                   │
                                          ┌────────▼─────────┐
                                          │ command_processor │
                                          │    (Executes)     │
                                          └──────────────────┘
```

## Files

| File | Purpose |
|------|---------|
| `bridge.py` | Telegram bot handler |
| `command_processor.py` | Processes queued commands |
| `start.sh` | Start both services |
| `stop.sh` | Stop both services |
| `check_commands.py` | Manual queue inspection |
| `.env` | API tokens |

## Logs

- Processor: `/tmp/command_processor.log`
- Bridge: `/tmp/bridge.log`

View logs:
```bash
tail -f /tmp/bridge.log
tail -f /tmp/command_processor.log
```

## Manual Queue Operations

List pending commands:
```bash
python3 check_commands.py
```

Add response manually:
```bash
python3 check_commands.py <cmd_id> "result text"
```

## Troubleshooting

### Commands not processing
Check if processor is running:
```bash
ps aux | grep command_processor
```

### Telegram not responding
Check if bridge is running:
```bash
ps aux | grep bridge
```

### View queue state
```bash
cat /tmp/claude_commands/queue.json
```
