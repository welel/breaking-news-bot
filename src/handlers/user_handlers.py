from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from config import load_config
from src.services.news import NewsClient
from src.services.storage import UserStorageClient
from src.services.storage.sqlitestorage import SQLiteUserStorage
from src.middlewares.storage import UserStorageMiddleware


router = Router()
config = load_config()
router.message.middleware(
    UserStorageMiddleware(UserStorageClient(SQLiteUserStorage(path=config.sqlite.path)))
)
NewsClient.set_api_key(config.newsapi.token)


@router.message(CommandStart())
async def process_start_command(
    message: Message, bot: Bot, user_storage: UserStorageClient
):
    await user_storage.save(message.from_user.id)
    await bot.send_message(
        message.chat.id,
        text="The bot delivers breaking news headlines related to technology.",
    )
    last_news = NewsClient.get_last_news()
    await bot.send_message(message.chat.id, text=last_news.title)


@router.message()
async def process_any_message(message: Message):
    await message.reply(text="The bot is not intended for messages. It sends the news.")
