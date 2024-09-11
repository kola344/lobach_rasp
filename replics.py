from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from datetime import datetime

import config
from date_functions import generate_date_range
import api

replic_hello = '😄 Привет! Я бот, который умеет выдавать расписание для группы\n➡️ Чтобы назначить себе свою группу, просто напиши мне её\nПример:\n3824Б1ПИ2'
replic_group_set_fail = '❌ Не удалось назначить группу. Проверь правильность написания группы.\nЕсли группа написана правильно, то, возможно, портал Лобачевского не работает'
replic_error = '😕 Ошибка. Проверь правильность написания команды, выбранную группу и роботоспособность портала ННГУ'

schedule_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Сегодня'), KeyboardButton(text='Завтра')],
                                        [KeyboardButton(text='Неделя'), KeyboardButton(text='Следующая')]],
                                        resize_keyboard=True)

def replic_group_set_success(group, desc):
    return f'✔️ Группа успешно назначена: {group}\n{desc}\n\n🔢 Нажимай на кнопки ниже, чтобы получить расписание\n✏️ Или введи "Неделя НОМЕР", чтобы получить расписание на соответствующее количество недель вперед', schedule_keyboard

async def replic_get_schedule(dates: list, group_id):
    text = '🗓️ Расписание\n'
    date_start, date_finish = dates[0], dates[1]
    days = generate_date_range(dates)
    data = await api.get_schedule(group_id, date_start, date_finish)
    if data is None:
        return '😕 Не удалось получить расписание. Проверь, выбрана ли у тебя группа или работает ли портал ННГУ'
    for day in days:
        need_add = False
        week_day = datetime.strptime(day, "%Y.%m.%d").weekday()
        add_text = f'📆 {day} - {config.days[week_day]}\n////////////////////\n'
        for i in data:
            if i['date'] == day:
                kindofOfWork = i['kindOfWork']
                sep_title = ''
                sep = ''
                if 'Лекция' in kindofOfWork:
                    sep_title = '📗'
                    sep = '🌵'
                elif 'Практика' in kindofOfWork:
                    sep_title = '📙'
                    sep = '🔶'
                elif 'Лабо' in kindofOfWork:
                    sep_title = '📘'
                    sep = '🔷'
                add_text += f'{sep_title} {i["beginLesson"]} - {i["endLesson"]} {i["kindOfWork"]}\n{i["discipline"]}\n{sep} {i["lecturer"]}\n{sep} {i["auditorium"]}[{i["building"]}]\n\n'
                need_add = True
        if need_add:
            text += f'{add_text}\n'
    return text
