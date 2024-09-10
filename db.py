import aiosqlite

class Database:
    def __init__(self):
        self.db = aiosqlite.connect("db.db")

    async def update_user(self, user_id, group):
        try:
            await self.db.execute('''UPDATE users SET group = ? WHERE user_id = ?''', (user_id, group))
        except:
            await self.db.execute('''INSERT INTO users (user_id, group) VALUES (?, ?)''', (user_id, group))

    async def get_user(self, user_id):
        async with self.db.execute('''SELECT group FROM users WHERE user_id = ?''', (user_id,)) as cursor:
            if len(await cursor.fetchall()) == 0:
                return None
            return await cursor.fetchone()[0]