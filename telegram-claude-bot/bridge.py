#!/usr/bin/env python3
"""
Telegram to Claude Code Bridge
Control your MacBook's Claude Code session from Telegram!

Commands:
- Just type normally -> Chat with Claude API directly
- /cmd <command> -> Execute command on MacBook
- /read <file> -> Read a file on MacBook
- /run <shell command> -> Run shell command
"""

import os
import json
import time
import asyncio
import uuid
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from anthropic import Anthropic

# Load environment variables
load_dotenv()

# Configuration
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Command queue file
QUEUE_FILE = "/tmp/claude_commands/queue.json"

# Initialize Anthropic client for direct chat
client = Anthropic(api_key=ANTHROPIC_API_KEY)

# Store chat conversation history
chat_conversations = {}

# Track commands awaiting confirmation (user_id -> cmd_id)
awaiting_confirmation = {}

def get_timestamp():
    return datetime.now().strftime("%H:%M:%S")

def load_queue():
    """Load command queue from file."""
    try:
        with open(QUEUE_FILE, 'r') as f:
            return json.load(f)
    except:
        return {"commands": [], "responses": {}}

def save_queue(queue):
    """Save command queue to file."""
    with open(QUEUE_FILE, 'w') as f:
        json.dump(queue, f, indent=2)

def add_command(user_id: int, command_type: str, content: str) -> str:
    """Add a command to the queue and return command ID."""
    queue = load_queue()
    cmd_id = str(uuid.uuid4())[:8]
    queue["commands"].append({
        "id": cmd_id,
        "user_id": user_id,
        "type": command_type,
        "content": content,
        "timestamp": datetime.now().isoformat(),
        "status": "pending"
    })
    save_queue(queue)
    return cmd_id

def get_response(cmd_id: str) -> dict:
    """Check if response is ready."""
    queue = load_queue()
    return queue["responses"].get(cmd_id)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome = """🤖 *Claude Code Bridge*

Control your MacBook's Claude Code from Telegram!

*Chat Mode:*
Just type a message to chat with Claude AI directly.

*Command Mode:*
`/cmd <text>` - Send command to Claude Code session
`/run <shell>` - Run shell command on MacBook
`/read <file>` - Read a file from MacBook
`/status` - Check pending commands
`/clear` - Clear chat history

*Confirmation:*
When a dangerous command is detected, you'll be asked to confirm.
`/confirm` - Approve the pending command
`/cancel` - Reject the pending command

*Example:*
`/cmd list all files in my projects folder`
`/run ls -la ~/Projects`
`/read /Users/colinyu/Projects/test.py`

Your commands will be queued and executed when Claude Code checks the queue."""
    await update.message.reply_text(welcome, parse_mode='Markdown')
    print(f"[{get_timestamp()}] User started bridge")

async def clear_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in chat_conversations:
        del chat_conversations[user_id]
    await update.message.reply_text("🧹 Chat history cleared!")
    print(f"[{get_timestamp()}] Chat history cleared")

async def check_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    queue = load_queue()
    pending = [c for c in queue["commands"] if c["status"] == "pending"]
    completed = len(queue["responses"])

    status = f"""📊 *Bridge Status*

⏳ Pending commands: {len(pending)}
✅ Completed: {completed}

*Pending:*
"""
    for cmd in pending[-5:]:
        status += f"• `{cmd['id']}`: {cmd['content'][:30]}...\n"

    await update.message.reply_text(status, parse_mode='Markdown')

async def send_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send command to Claude Code session."""
    user_id = update.effective_user.id

    if not context.args:
        await update.message.reply_text("Usage: /cmd <your command>\nExample: /cmd read the file bot.py")
        return

    content = " ".join(context.args)
    cmd_id = add_command(user_id, "claude_command", content)

    await update.message.reply_text(
        f"📤 Command queued!\n\n"
        f"ID: `{cmd_id}`\n"
        f"Type: Claude Command\n"
        f"Content: {content[:50]}...\n\n"
        f"⏳ Waiting for Claude Code to process...\n"
        f"Use /status to check progress",
        parse_mode='Markdown'
    )
    print(f"[{get_timestamp()}] Command queued: {cmd_id} - {content[:50]}")

async def run_shell(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Run shell command."""
    user_id = update.effective_user.id

    if not context.args:
        await update.message.reply_text("Usage: /run <shell command>\nExample: /run ls -la ~/Projects")
        return

    content = " ".join(context.args)
    cmd_id = add_command(user_id, "shell_command", content)

    await update.message.reply_text(
        f"📤 Shell command queued!\n\n"
        f"ID: `{cmd_id}`\n"
        f"Command: `{content}`\n\n"
        f"⏳ Waiting for execution...",
        parse_mode='Markdown'
    )
    print(f"[{get_timestamp()}] Shell queued: {cmd_id} - {content}")

async def read_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Read file command."""
    user_id = update.effective_user.id

    if not context.args:
        await update.message.reply_text("Usage: /read <file path>\nExample: /read /Users/colinyu/Projects/bot.py")
        return

    filepath = " ".join(context.args)
    cmd_id = add_command(user_id, "read_file", filepath)

    await update.message.reply_text(
        f"📤 File read queued!\n\n"
        f"ID: `{cmd_id}`\n"
        f"File: `{filepath}`\n\n"
        f"⏳ Waiting for Claude Code to read...",
        parse_mode='Markdown'
    )
    print(f"[{get_timestamp()}] Read queued: {cmd_id} - {filepath}")

async def confirm_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle user confirmation for a pending command."""
    user_id = update.effective_user.id

    if user_id not in awaiting_confirmation:
        await update.message.reply_text("❌ No command awaiting confirmation.")
        return

    original_cmd_id = awaiting_confirmation[user_id]

    # Add confirmation response to queue
    cmd_id = add_command(user_id, "confirmation_response", "confirm")
    queue = load_queue()

    # Link to original command
    for cmd in queue["commands"]:
        if cmd["id"] == cmd_id:
            cmd["original_cmd_id"] = original_cmd_id
            break
    save_queue(queue)

    # Clear awaiting confirmation
    del awaiting_confirmation[user_id]

    await update.message.reply_text(
        f"✅ Confirmation sent!\n\n"
        f"Proceeding with command `{original_cmd_id}`...",
        parse_mode='Markdown'
    )
    print(f"[{get_timestamp()}] Confirmation received for {original_cmd_id}")

async def cancel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle user cancellation for a pending command."""
    user_id = update.effective_user.id

    if user_id not in awaiting_confirmation:
        await update.message.reply_text("❌ No command awaiting confirmation.")
        return

    original_cmd_id = awaiting_confirmation[user_id]

    # Add cancellation response to queue
    cmd_id = add_command(user_id, "confirmation_response", "cancel")
    queue = load_queue()

    # Link to original command
    for cmd in queue["commands"]:
        if cmd["id"] == cmd_id:
            cmd["original_cmd_id"] = original_cmd_id
            break
    save_queue(queue)

    # Clear awaiting confirmation
    del awaiting_confirmation[user_id]

    await update.message.reply_text(
        f"❌ Command cancelled!\n\n"
        f"Command `{original_cmd_id}` will not be executed.",
        parse_mode='Markdown'
    )
    print(f"[{get_timestamp()}] Command {original_cmd_id} cancelled")

async def chat_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle regular chat messages - direct to Claude API."""
    user = update.effective_user
    user_id = user.id
    message = update.message.text

    print(f"[{get_timestamp()}] Chat from {user.first_name}: {message[:50]}...")

    # Show typing
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    # Get conversation history
    if user_id not in chat_conversations:
        chat_conversations[user_id] = []

    try:
        # Call Claude API directly for chat
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1500,
            system="You are Claude, a helpful AI assistant. Respond conversationally.",
            messages=chat_conversations[user_id] + [{"role": "user", "content": message}]
        )

        reply = response.content[0].text

        # Update history
        chat_conversations[user_id].append({"role": "user", "content": message})
        chat_conversations[user_id].append({"role": "assistant", "content": reply})

        # Keep last 20 messages
        if len(chat_conversations[user_id]) > 20:
            chat_conversations[user_id] = chat_conversations[user_id][-20:]

        # Send response
        if len(reply) > 4000:
            for chunk in [reply[i:i+4000] for i in range(0, len(reply), 4000)]:
                await update.message.reply_text(chunk)
        else:
            await update.message.reply_text(reply)

        print(f"[{get_timestamp()}] Chat reply sent")

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")
        print(f"[{get_timestamp()}] Error: {e}")

async def response_checker(application):
    """Background task to check for responses and send them."""
    while True:
        try:
            queue = load_queue()

            # Check for commands that might have responses
            for cmd in queue["commands"]:
                if cmd["status"] == "pending":
                    continue

                response = queue["responses"].get(cmd["id"])
                if not response:
                    continue

                # Check if already sent
                if response.get("sent"):
                    continue

                result = response.get("result", "No result")
                if len(result) > 4000:
                    result = result[:4000] + "\n... (truncated)"

                # Check if this requires confirmation
                if response.get("requires_confirmation") or cmd["status"] == "awaiting_confirmation":
                    # Track this command as awaiting confirmation
                    awaiting_confirmation[cmd["user_id"]] = cmd["id"]

                    # Mark as sent
                    response["sent"] = True
                    save_queue(queue)

                    try:
                        await application.bot.send_message(
                            chat_id=cmd["user_id"],
                            text=f"⚠️ *Confirmation Required*\n\nID: `{cmd['id']}`\n\n{result}\n\n"
                                 f"Reply with /confirm to proceed or /cancel to abort.",
                            parse_mode='Markdown'
                        )
                        print(f"[{get_timestamp()}] Confirmation request sent for {cmd['id']}")
                    except Exception as e:
                        print(f"[{get_timestamp()}] Failed to send confirmation: {e}")
                else:
                    # Mark as completed
                    cmd["status"] = "completed"
                    response["sent"] = True
                    save_queue(queue)

                    # Send response to user
                    try:
                        await application.bot.send_message(
                            chat_id=cmd["user_id"],
                            text=f"✅ *Command Complete*\n\nID: `{cmd['id']}`\n\n```\n{result}\n```",
                            parse_mode='Markdown'
                        )
                        print(f"[{get_timestamp()}] Response sent for {cmd['id']}")
                    except Exception as e:
                        print(f"[{get_timestamp()}] Failed to send response: {e}")

            await asyncio.sleep(2)  # Check every 2 seconds

        except Exception as e:
            print(f"[{get_timestamp()}] Checker error: {e}")
            await asyncio.sleep(5)

def main():
    print("=" * 50)
    print("Telegram → Claude Code Bridge")
    print("=" * 50)

    if not TELEGRAM_BOT_TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN not set!")
        exit(1)

    # Create application with post_init for background task
    async def post_init(app):
        asyncio.create_task(response_checker(app))

    application = (
        Application.builder()
        .token(TELEGRAM_BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", start))
    application.add_handler(CommandHandler("clear", clear_chat))
    application.add_handler(CommandHandler("status", check_status))
    application.add_handler(CommandHandler("cmd", send_command))
    application.add_handler(CommandHandler("run", run_shell))
    application.add_handler(CommandHandler("read", read_file))
    application.add_handler(CommandHandler("confirm", confirm_command))
    application.add_handler(CommandHandler("cancel", cancel_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_message))

    print(f"✅ Bridge ready!")
    print(f"📱 Open Telegram and send /start")
    print(f"📤 Commands will be queued at: {QUEUE_FILE}")
    print("-" * 50)
    print("Press Ctrl+C to stop")
    print("=" * 50)

    # Start polling
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
