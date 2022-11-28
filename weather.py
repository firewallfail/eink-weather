import requests
import json
import time

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

    sunrise = ttk.Label(sun_stats, text=sun_rise)
    sunrise.grid(row=0, column=1, sticky=N)
    sunset = ttk.Label(sun_stats, text=sun_set)
    sunset.grid(row=1, column=1, sticky=N)

    window.after(next_update, get_sun_stats) # once per day


def get_sun_stats():
    
    lat = 42.984924
    lng = -81.245277

    sun_api = f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}'
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

date = ttk.Label(window, text="Date")
date.grid(row=1, column=0, sticky=N)

unknown = ttk.Label(window, text="Undecided")
unknown.grid(row=1, column=1, sticky=N)

get_sun_stats()


window.geometry("800x480")
window.mainloop()