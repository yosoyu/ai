#!/usr/bin/env python3
"""
Telegram to Claude Bot
Chat with Claude from your phone via Telegram!

Setup:
1. Create a bot with @BotFather on Telegram
2. Install dependencies: pip install python-telegram-bot anthropic python-dotenv
3. Create .env file with your tokens
4. Run: python bot.py
"""

import os
import asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from anthropic import Anthropic

# Load environment variables
load_dotenv()

# Configuration
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ALLOWED_USERS = os.getenv("ALLOWED_USERS", "").split(",") if os.getenv("ALLOWED_USERS") else []

# System prompt for Claude
SYSTEM_PROMPT = """You are a helpful AI assistant. The user is messaging you from Telegram on their phone.
Keep your responses:
- Concise and helpful
- Well-formatted (Telegram supports Markdown)
- Friendly and conversational
- You are Colin's personal AI assistant"""

# Initialize Anthropic client
client = Anthropic(api_key=ANTHROPIC_API_KEY)

# Store conversation history (user_id -> list of messages)
conversations = {}

def is_allowed_user(user_id: int) -> bool:
    """Check if user is in the allowed list."""
    if not ALLOWED_USERS or ALLOWED_USERS == [""]:
        return True  # Allow all if whitelist is empty
    return str(user_id) in ALLOWED_USERS

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command."""
    user = update.effective_user
    welcome_msg = f"""👋 Hello {user.first_name}!

I'm Claude, connected via Telegram. You can chat with me just like in the Claude app!

Commands:
/start - Show this message
/clear - Clear conversation history
/help - Show help

Just send me a message to start chatting!"""
    await update.message.reply_text(welcome_msg)
    print(f"[{get_timestamp()}] User {user.first_name} ({user.id}) started the bot")

async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /clear command - clear conversation history."""
    user_id = update.effective_user.id
    if user_id in conversations:
        del conversations[user_id]
    await update.message.reply_text("🧹 Conversation history cleared!")
    print(f"[{get_timestamp()}] User {user_id} cleared conversation")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command."""
    help_text = """🤖 *Claude Telegram Bot*

This bot connects you to Claude AI from your phone.

*Commands:*
/start - Initialize the bot
/clear - Reset conversation memory
/help - Show this message

*Features:*
• Remembers conversation context
• Supports markdown formatting
• Available 24/7

Just type your message and Claude will respond!"""
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming text messages."""
    user = update.effective_user
    user_id = user.id
    message_text = update.message.text

    # Check if user is allowed
    if not is_allowed_user(user_id):
        await update.message.reply_text("⚠️ Sorry, you're not authorized to use this bot.")
        return

    print(f"[{get_timestamp()}] Message from {user.first_name} ({user_id}): {message_text[:50]}...")

    # Show typing indicator
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    # Get or create conversation history
    if user_id not in conversations:
        conversations[user_id] = []

    # Call Claude API
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            system=SYSTEM_PROMPT,
            messages=conversations[user_id] + [{"role": "user", "content": message_text}]
        )

        claude_response = response.content[0].text

        # Update conversation history
        conversations[user_id].append({"role": "user", "content": message_text})
        conversations[user_id].append({"role": "assistant", "content": claude_response})

        # Keep only last 40 messages (20 exchanges)
        if len(conversations[user_id]) > 40:
            conversations[user_id] = conversations[user_id][-40:]

        # Send response (Telegram has 4096 char limit, split if needed)
        if len(claude_response) > 4000:
            # Split long messages
            chunks = [claude_response[i:i+4000] for i in range(0, len(claude_response), 4000)]
            for chunk in chunks:
                await update.message.reply_text(chunk)
        else:
            await update.message.reply_text(claude_response)

        print(f"[{get_timestamp()}] Response sent to {user.first_name}")

    except Exception as e:
        error_msg = f"❌ Error: {str(e)}"
        await update.message.reply_text(error_msg)
        print(f"[{get_timestamp()}] Error: {e}")

def get_timestamp():
    """Get current timestamp string."""
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")

def main():
    """Start the bot."""
    print("=" * 50)
    print("Telegram Claude Bot Starting...")
    print("=" * 50)

    # Validate configuration
    if not TELEGRAM_BOT_TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN not set!")
        exit(1)

    if not ANTHROPIC_API_KEY:
        print("Error: ANTHROPIC_API_KEY not set!")
        exit(1)

    # Create application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("clear", clear_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print(f"✅ Bot configured successfully!")
    print(f"📱 Open Telegram and search for your bot")
    print(f"💬 Send /start to begin")
    print("-" * 50)
    print("Press Ctrl+C to stop")
    print("=" * 50)

    # Start polling
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
