import requests
import json
import time
import constants as CONS

from tkinter import ttk, Tk, N, S, E, W
from dateutil import tz
from datetime import datetime, timedelta
from random import randint


def time_to_local(time):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    utc = datetime.strptime(time, '%I:%M:%S %p')
    utc = utc.replace(tzinfo=from_zone)
    local = utc.astimezone(to_zone)

    return local.strftime('%I:%M:%S %p')


def draw_sun_stats(next_update, sun_rise, sun_set):
    sun_stats = ttk.Frame(window)
    sun_stats.grid(row=1, column=2)

    sunrise = ttk.Label(sun_stats, text=f'Sun Rise: {sun_rise}')
    sunrise.grid(row=0, column=1, sticky=N)
    sunset = ttk.Label(sun_stats, text=f'Sun Set: {sun_set}')
    sunset.grid(row=1, column=1, sticky=N)

    window.after(next_update, get_sun_stats) # once per day


def get_sun_stats():
    sun_api = f'https://api.sunrise-sunset.org/json?lat={CONS.LAT}&lng={CONS.LNG}'
    results = requests.get(sun_api).json().get('results', None)

    if not results:
        thirty_mins_in_ms = 30 * 60 * 1000
        draw_sun_stats(thirty_mins_in_ms, 'Error', 'Other Error')
        return False

    sun_rise = time_to_local(results['sunrise'])
    sun_set = time_to_local(results['sunset'])

    current_time = datetime.now()
    midnight = (current_time + timedelta(days=1)).replace(hour=0, minute=0)
    next_update = ((midnight - current_time).seconds) * 1000 # ms until next update after midnight
    draw_sun_stats(next_update, sun_rise, sun_set)

    return True


def get_date_stats():
    current_time = datetime.now()
    midnight = (current_time + timedelta(days=1)).replace(hour=0, minute=0)
    next_update = ((midnight - current_time).seconds) * 1000 # ms until next update after midnight
    date = {
        'weekday': CONS.WEEKDAYS[datetime.today().weekday()],
        'month': CONS.MONTHS[datetime.today().month - 1],
        'day': datetime.today().day,
        'year': datetime.today().year
    }
    draw_date_tile(next_update, date)


def draw_date_tile(next_update, datestamp):
    date = ttk.Frame(window)
    date.grid(row=1, column=0)
    title = ttk.Label(date, text="Date")
    title.grid(row=0, column=0)
    weekday = ttk.Label(date, text=datestamp['weekday'])
    weekday.grid(row=1, column=0)
    month = ttk.Label(date, text=datestamp['month'])
    month.grid(row=2, column=0)
    day = ttk.Label(date, text=datestamp['day'])
    day.grid(row=3, column=0)
    year = ttk.Label(date, text=datestamp['year'])
    year.grid(row=4, column=0)

    window.after(next_update, get_date_stats) # once per day


def get_weather_stats():
    weather_api = f'https://api.open-meteo.com/v1/forecast?latitude={CONS.LAT}&longitude={CONS.LNG}&hourly=temperature_2m,precipitation,weathercode&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,precipitation_sum&timezone=auto'
    return


def draw_weather_tiles():
    return


window = Tk()
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)




current_weather = ttk.Label(window, text="Current Weather")
current_weather.grid(row=0, column=0, sticky=N)

next_hour = ttk.Label(window, text="Next Hour")
next_hour.grid(row=0, column=1, sticky=N)

tomorrow_weather = ttk.Label(window, text="Tomorrows Weather")
tomorrow_weather.grid(row=0, column=2, sticky=N)

get_date_stats()

unknown = ttk.Label(window, text="Undecided")
unknown.grid(row=1, column=1, sticky=N)

get_sun_stats()


window.geometry("800x480")
window.mainloop()