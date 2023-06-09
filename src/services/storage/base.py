"""This module contains abstractions for the user storage.

Classes:

    UserStorageInterface: An abstract base class for user storage.
    UserStorageClient: A class that serves as a client to interact
        with the user storage.

"""
import abc


class UserStorageInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "save")
            and callable(subclass.save)
            and hasattr(subclass, "all")
            and callable(subclass.all)
            and hasattr(subclass, "delete")
            and callable(subclass.delete)
            or NotImplemented
        )

    @abc.abstractmethod
    async def save(self, user_id: int) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    async def all(self) -> tuple[int]:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete(self, user_id: int) -> None:
        raise NotImplementedError


class UserStorageClient(UserStorageInterface):
    def __init__(self, storage: UserStorageInterface):
        self.storage = storage

    async def save(self, user_id: int) -> None:
        return await self.storage.save(user_id)

    async def all(self) -> tuple[int]:
        return await self.storage.all()

    async def delete(self, user_id: int) -> None:
        return await self.storage.delete(user_id)
