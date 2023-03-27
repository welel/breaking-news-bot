import sqlite3

import aiosqlite

from .base import UserStorageInterface


class SQLiteUserStorage(UserStorageInterface):
    """A user storage implementation that stores user IDs in an SQLite database.

    Attributes:
        path (str): The path to the SQLite database file.
        user_table_name (str): The name of the table that stores user IDs.

    """

    def __init__(self, path: str):
        self.path = path
        self.user_table_name = "users"
        self._init_database()

    def _init_database(self):
        """Initializes the database by creating a user table if it doesn't exist."""
        with sqlite3.connect(self.path) as db:
            cursor = db.cursor()

            # Creates a user table if it doesn't exist
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS users
                                (id INTEGER PRIMARY KEY,
                                user_id INTEGER UNIQUE)"""
            )

    async def save(self, user_id: int) -> None:
        async with aiosqlite.connect(self.path) as db:
            await db.execute(
                "INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,)
            )
            await db.commit()

    async def all(self) -> tuple[int]:
        async with aiosqlite.connect(self.path) as db:
            async with db.execute("SELECT * FROM users") as cursor:
                users = await cursor.fetchall()
                return tuple([user_id for _, user_id in users])

    async def delete(self, user_id: int) -> None:
        async with aiosqlite.connect(self.path) as db:
            await db.execute("DELETE FROM users WHERE user_id=?", (user_id,))
            await db.commit()
