from fastapi import FastAPI
from bot_init import bot, dp
from typing import Any
from aiogram.types import Update
from db_init import initialise
import config
from bot import router

app = FastAPI()

@app.post('/webhook')
async def webhook(update: dict[str, Any]):
    '''АХАХАХХАХАХАХАХАХАХАХ'''
    await dp.feed_webhook_update(bot=bot, update=Update(**update))
    return {'status': 'ok'}

@app.on_event('startup')
async def startup():
    await initialise()
    await dp.include_router(router)
    await bot.set_webhook(config.webhook_url, drop_pending_updates=True)