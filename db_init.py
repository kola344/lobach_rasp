import db

users = db.Database()

async def initialise():
    await users.connect()