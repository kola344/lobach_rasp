bot_token = "7210602245:AAHeAS-Pi_hqJshXQIVrPuaTS7H3WvoaY2I"

api_url_groups = 'https://portal.unn.ru/ruzapi/search'
#term, type=group
api_url_get_schelude = f'https://portal.unn.ru/ruzapi/schedule/group/%group_id%'
#%group_id%, start=(date), finish=(date), lng=1
days = {
    0: 'Понедельник',
    1: 'Вторник',
    2: 'Среда',
    3: 'Четверг',
    4: 'Пятница',
    5: 'Суббота',
    6: 'Воскресенье'
}

webhook_url = 'localhost/webhook'