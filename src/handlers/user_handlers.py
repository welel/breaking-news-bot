from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from services.news import NewsClient
from services.storage import StorageClient


router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message, bot: Bot):
    await StorageClient.save_user(message.from_user.id)
    await bot.send_message(message.chat.id, text="The bot ...")
    last_message = NewsClient.get_last_news()
    await bot.send_message()  # send news


@router.message()
async def process_any_message(message: Message):
    await message.reply(text="The bot is not intended for messages. It sends the news.")
