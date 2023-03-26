import asyncio
import os
import sqlite3

import aiosqlite

# from .base import UserStorageInterface


class SQLiteUserStorageClient:  # (UserStorageInterface):
    def __init__(self, path: str):
        self.path = path
        self.user_table_name = "users"
        self._init_database()

    def _init_database(self):
        with sqlite3.connect(self.path) as db:
            cursor = db.cursor()

            # Execute a query to check if the table exists
            cursor.execute(
                f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.user_table_name}'"
            )
            if cursor.fetchone() is None:
                # Create databse
                cursor.execute(
                    str(
                        "CREATE TABLE users "
                        "(id INTEGER PRIMARY KEY, "
                        "user_id INTEGER)"
                    )
                )

    async def test_connection(self):
        async with aiosqlite.connect("sqlite.db") as db:
            return await db.execute("SELECT	1 + 1;")


async def main():
    storage = SQLiteUserStorageClient(path="sql.db")
    print(await storage.test_connection())


if __name__ == "__main__":
    asyncio.run(main())
