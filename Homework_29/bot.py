import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters
)

from weather import get_weather

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

user_state = {}


async def start(update: Update) -> None:
    """Handle /start command"""
    await update.message.reply_text(
        "Вітаю! Я бот погоди.\n"
        "Доступні команди:\n"
        "/weather — дізнатися погоду\n"
        "/help — довідка"
    )


async def help_command(update: Update) -> None:
    """Handle /help command"""
    await update.message.reply_text(
        "/start — почати роботу\n"
        "/weather — отримати погоду в місті"
    )


async def weather_command(update: Update) -> None:
    """Ask user for city name"""
    user_state[update.effective_user.id] = "WAITING_FOR_CITY"
    await update.message.reply_text("Вкажіть місто:")


async def handle_message(update: Update) -> None:
    """Handle city input"""
    user_id = update.effective_user.id

    if user_state.get(user_id) == "WAITING_FOR_CITY":
        city = update.message.text
        result = get_weather(city)
        await update.message.reply_text(result)
        user_state.pop(user_id, None)


def main() -> None:
    """Start the bot"""
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("weather", weather_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logging.info("Bot started")
    app.run_polling()


if __name__ == "__main__":
    main()
