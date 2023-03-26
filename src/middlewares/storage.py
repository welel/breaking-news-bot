from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message

from src.services.storage import UserStorageClient


class UserStorageMiddleware(BaseMiddleware):
    def __init__(self, user_storage: UserStorageClient) -> None:
        self.user_storage = user_storage

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        data["user_storage"] = self.user_storage
        return await handler(event, data)
