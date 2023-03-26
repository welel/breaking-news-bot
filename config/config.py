from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

from .base import getenv, ImproperlyConfigured


@dataclass
class TelegramBotConfig:
    token: str


@dataclass
class NewsAPIConfig:
    token: str


@dataclass
class SQLiteConfig:
    path: str


@dataclass
class Config:
    tg_bot: TelegramBotConfig
    newsapi: NewsAPIConfig
    sqlite: SQLiteConfig


def load_config() -> Config:
    # Parse a `.env` file and load the variables into environment valriables
    load_dotenv()

    BASE_DIR: str = Path(__file__).resolve().parent.parent

    return Config(
        tg_bot=TelegramBotConfig(token=getenv("BOT_TOKEN")),
        newsapi=NewsAPIConfig(token=getenv("NEWSAPI_TOKEN")),
        sqlite=SQLiteConfig(path=Path.joinpath(BASE_DIR, getenv("SQLITE_PATH"))),
    )
