import aiosqlite
import asyncio


class Database:
    def __init__(self):
        self.db = None

    async def connect(self):
        self.db = await aiosqlite.connect("db.db")

    async def update_user(self, user_id, group, group_id):
        async with self.db.execute('''SELECT 1 FROM users WHERE user_id = ?''', (user_id,)) as cursor:
            exists = await cursor.fetchone()

        if exists:
            await self.db.execute('''UPDATE users SET "group" = ?, group_id = ? WHERE user_id = ?''',
                                  (group, group_id, user_id))
        else:
            await self.db.execute('''INSERT INTO users (user_id, "group", group_id) VALUES (?, ?, ?)''',
                                  (user_id, group, group_id))

        await self.db.commit()

    async def get_user_group_id(self, user_id):
        async with self.db.execute('''SELECT group_id FROM users WHERE user_id = ?''', (user_id,)) as cursor:
            row = await cursor.fetchone()
            if row is None:
                return None
            return row[0]

    async def get_users_count(self):
        async with self.db.execute('''SELECT * FROM users''') as cursor:
            return len(await cursor.fetchall())

    async def get_users(self):
        async with self.db.execute('''SELECT * FROM users''') as cursor:
            users = await cursor.fetchall()
            result = [{"user_id": i[0], "group": i[1], "group_id": i[2]} for i in users]
            return result





async def db_initialise():
    db = Database()
    await db.connect()
    return db
