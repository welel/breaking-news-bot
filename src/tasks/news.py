import asyncio
import logging

from aiogram import Bot

from config import load_config
from src.services.news import NewsClient
from src.services.storage import UserStorageClient
from src.formatters.news import news_format

NewsClient.set_api_key(load_config().newsapi.token)


async def send_last_news_to_users(bot: Bot, user_storage: UserStorageClient):
    new_news = NewsClient.get_new_news_list()
    users_ids = await user_storage.all()

    for news in new_news:
        for user_id in users_ids:
            try:
                await bot.send_message(
                    user_id, text=news_format(news), disable_notification=True
                )
            except Exception as e:
                logging.error(
                    f"[SendNewsFaild]: {e}; user id {user_id}; {type(news)}; {news}"
                )
            await asyncio.sleep(1)
