"""
Navigator Bot Listener
Runs permanently and handles /addme, /removeme, /status commands.
Users self-onboard — no manual chat ID hunting needed.
Run with: python3 bot_listener.py
"""

import json
import os
import asyncio
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_CHAT_ID = 1357019604  # Nardus — gets notified of new subscribers
SUBSCRIBERS_FILE = "subscribers.json"

def load_subscribers():
    try:
        with open(SUBSCRIBERS_FILE) as f:
            return json.load(f)
    except:
        return []

def save_subscribers(subs):
    with open(SUBSCRIBERS_FILE, "w") as f:
        json.dump(subs, f, indent=2)

def find_subscriber(subs, chat_id):
    return next((s for s in subs if s["chat_id"] == chat_id), None)

async def cmd_addme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat_id = update.effective_chat.id
    subs = load_subscribers()

    if find_subscriber(subs, chat_id):
        await update.message.reply_text(
            "✅ You're already on the Navigator daily briefing list!\n"
            "You'll receive your briefing every morning at 05:30 CAT."
        )
        return

    subs.append({
        "chat_id": chat_id,
        "name": f"{user.first_name} {user.last_name or ''}".strip(),
        "username": user.username or "",
        "joined": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    save_subscribers(subs)

    await update.message.reply_text(
        f"🧭 *Welcome to Navigator, {user.first_name}!*\n\n"
        f"You'll receive the daily briefing every morning at 05:30 CAT.\n\n"
        f"Commands:\n"
        f"• /addme — join the briefing\n"
        f"• /removeme — leave the briefing\n"
        f"• /status — check your subscription\n"
        f"• /subscribers — list all subscribers (admin only)\n\n"
        f"_Navigator out._ ⚡",
        parse_mode="Markdown"
    )

    # Notify Nardus
    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f"🟢 *New Navigator subscriber!*\n"
             f"Name: {user.first_name} {user.last_name or ''}\n"
             f"Username: @{user.username or 'no username'}\n"
             f"Chat ID: {chat_id}\n"
             f"Total subscribers: {len(subs)}",
        parse_mode="Markdown"
    )

async def cmd_removeme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    subs = load_subscribers()
    user = update.effective_user

    if not find_subscriber(subs, chat_id):
        await update.message.reply_text("You're not currently on the briefing list.")
        return

    subs = [s for s in subs if s["chat_id"] != chat_id]
    save_subscribers(subs)

    await update.message.reply_text(
        f"👋 You've been removed from Navigator briefings, {user.first_name}.\n"
        f"Send /addme anytime to rejoin."
    )

    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f"🔴 *Subscriber left:* {user.first_name} {user.last_name or ''}\n"
             f"Remaining subscribers: {len(subs)}",
        parse_mode="Markdown"
    )

async def cmd_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    subs = load_subscribers()
    sub = find_subscriber(subs, chat_id)

    if sub:
        await update.message.reply_text(
            f"✅ *You're subscribed to Navigator*\n"
            f"Joined: {sub['joined']}\n"
            f"Briefing time: 05:30 CAT daily",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(
            "❌ You're not subscribed. Send /addme to join."
        )

async def cmd_subscribers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id != ADMIN_CHAT_ID:
        await update.message.reply_text("⛔ Admin only.")
        return

    subs = load_subscribers()
    if not subs:
        await update.message.reply_text("No subscribers yet.")
        return

    msg = f"📋 *Navigator Subscribers ({len(subs)})*\n\n"
    for s in subs:
        msg += f"• {s['name']} (@{s.get('username', 'none')}) — joined {s['joined']}\n"

    await update.message.reply_text(msg, parse_mode="Markdown")

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"🧭 *Welcome to Navigator, {user.first_name}!*\n\n"
        f"Navigator is the daily intelligence briefing for COTRUGLI Vanguard MBA students.\n\n"
        f"Send /addme to subscribe to the daily briefing at 05:30 CAT.\n\n"
        f"_Built by Nardus Du Plooy · Team Chiron_",
        parse_mode="Markdown"
    )

def main():
    print("🧭 Navigator Bot Listener starting...")
    print("📡 Listening for /addme, /removeme, /status commands")
    print("Press CTRL+C to stop\n")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("addme", cmd_addme))
    app.add_handler(CommandHandler("removeme", cmd_removeme))
    app.add_handler(CommandHandler("status", cmd_status))
    app.add_handler(CommandHandler("subscribers", cmd_subscribers))

    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
