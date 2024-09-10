import aiogram
from aiogram import Bot, Dispatcher
from aiogram import types
from bot_init import dp, bot
import asyncio


async def bot_starter():
    print('virazh running')

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

async def main():
    await bot_starter()

if __name__ == '__main__':
    print('virazh bot running')
    asyncio.run(main())