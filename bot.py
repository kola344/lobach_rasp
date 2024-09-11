import date_functions
from bot_init import dp, bot
import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, FSInputFile
from replics import *
import api
from db_init import users, initialise
from datetime import datetime, timedelta
import traceback

router = Router()

@router.message(F.text == '/start')
async def start(message: Message):
    await message.answer(replic_hello)

@router.message(F.text == 'Неделя')
async def week(message: Message):
    group_id = await users.get_user_group_id(message.from_user.id)
    monday, sunday = date_functions.get_week_dates()
    text = await replic_get_schedule([monday, sunday], group_id)
    await message.answer(text)

@router.message(F.text.startswith('Неделя'))
async def custom_week(message: Message):
    try:
        splited_message = message.text.split()
        custom_week = splited_message[1]
        group_id = await users.get_user_group_id(message.from_user.id)
        monday, sunday = date_functions.get_custom_week_dates(int(custom_week))
        text = await replic_get_schedule([monday, sunday], group_id)
        await message.answer(text)
    except:
        traceback.print_exc()
        await message.answer(replic_error)

@router.message(F.text == 'Сегодня')
async def today(message: Message):
    group_id = await users.get_user_group_id(message.from_user.id)
    date = datetime.now().strftime('%Y.%m.%d')
    text = await replic_get_schedule([date, date], group_id)
    await message.answer(text)

@router.message(F.text == 'Следующая')
async def next_week(message: Message):
    group_id = await users.get_user_group_id(message.from_user.id)
    monday, sunday = date_functions.get_next_week_dates()
    text = await replic_get_schedule([monday, sunday], group_id)
    await message.answer(text)

@router.message(F.text == 'Завтра')
async def tomorrow(message: Message):
    group_id = await users.get_user_group_id(message.from_user.id)
    date = (datetime.now() + timedelta(days=1)).strftime("%Y.%m.%d")
    text = await replic_get_schedule([date, date], group_id)
    await message.answer(text)

@router.message()
async def set_group(message: Message):
    try:
        group_id, group, desc = await api.get_group_id(message.text)
        if group_id:
            await users.update_user(message.from_user.id, message.text, group_id)
            text, markup = replic_group_set_success(group, desc)
            await message.answer(text, reply_markup=markup)
        else:
            await message.answer(replic_group_set_fail)
    except:
        await message.answer(replic_group_set_fail)




async def bot_starter():
    print('started')
    await initialise()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

async def main():
    await bot_starter()

if __name__ == '__main__':
    print("running")
    asyncio.run(main())