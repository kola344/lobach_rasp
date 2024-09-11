from datetime import datetime, timedelta


def generate_date_range(date_list):
    start_date = datetime.strptime(date_list[0], "%Y.%m.%d")
    end_date = datetime.strptime(date_list[1], "%Y.%m.%d")

    date_range = []

    current_date = start_date
    while current_date <= end_date:
        date_range.append(current_date.strftime("%Y.%m.%d"))
        current_date += timedelta(days=1)

    return date_range

from datetime import datetime, timedelta

def get_week_dates():
    today = datetime.now()
    monday = (today - timedelta(days=today.weekday())).strftime("%Y.%m.%d")
    sunday = (today + timedelta(days=6 - today.weekday())).strftime("%Y.%m.%d")
    return monday, sunday

from datetime import datetime, timedelta

def get_next_week_dates():
    today = datetime.now()
    next_monday = (today + timedelta(days=-today.weekday() + 7)).strftime("%Y.%m.%d")
    next_sunday = (today + timedelta(days=-today.weekday() + 13)).strftime("%Y.%m.%d")
    return next_monday, next_sunday

def get_custom_week_dates(week):
    today = datetime.now()
    week_monday = (today + timedelta(days=-today.weekday() + 7+(week*7))).strftime("%Y.%m.%d")
    week_sunday = (today + timedelta(days=-today.weekday() + 13+(week*7))).strftime("%Y.%m.%d")
    return week_monday, week_sunday

