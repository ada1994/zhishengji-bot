import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 请将 YOUR_TOKEN 替换为你的 BotFather Token
import os
token = os.environ.get("TOKEN")

WELCOME_TEXT = (
    "您好，欢迎咨询直升机/机票/旅游业务。\n"
    "请直接联系客服 @Boatbabes，我们会第一时间为您服务！"
)

CONTACT_BUTTON = InlineKeyboardMarkup([
    [InlineKeyboardButton("联系客服", url="https://t.me/Boatbabes")]
])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT, reply_markup=CONTACT_BUTTON)
    # 通知你（@Boatbabes）有新用户点击了 /start
    user = update.effective_user
    msg = f"有新客户点击了 /start\n用户名: @{user.username if user.username else '无'}\n姓名: {user.full_name}\n用户ID: {user.id}"
    # 你的 Telegram 用户ID，可以用 @userinfobot 获取
    admin_id = 7158664620  # 用户的真实 Telegram 用户ID
    try:
        await context.bot.send_message(chat_id=admin_id, text=msg)
    except Exception as e:
        logging.error(f"通知管理员失败: {e}")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT, reply_markup=CONTACT_BUTTON)

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, echo))
    app.run_polling()
