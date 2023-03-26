import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from aiogram import Bot, Dispatcher

from config import Config, load_config
from src.handlers import user_handlers
from src.middlewares.storage import UserStorageMiddleware
from src.services.storage import UserStorageClient
from src.services.storage.sqlitestorage import SQLiteUserStorage
from src.tasks.news import send_last_news_to_users


logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

    logger.info("Starting bot")

    config: Config = load_config()

    user_storage: UserStorageClient = UserStorageClient(
        SQLiteUserStorage(path=config.sqlite.path)
    )

    scheduler = AsyncIOScheduler()

    bot: Bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dp: Dispatcher = Dispatcher()

    user_handlers.router.message.middleware(UserStorageMiddleware(user_storage))
    dp.include_router(user_handlers.router)

    scheduler.add_job(
        send_last_news_to_users, "cron", hour="*", args=(bot, user_storage)
    )
    scheduler.start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
