import requests
import json
import time

from tkinter import *
from tkinter import ttk
from dateutil import tz
from datetime import datetime, timedelta


def time_to_local(time):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    utc = datetime.strptime(time, '%I:%M:%S %p')
    utc = utc.replace(tzinfo=from_zone)
    local = utc.astimezone(to_zone)

    return local


def get_sun_stats():
    lat = 42.984924
    lng = -81.245277
    # temp hardcode time to stop hitting api needlessly
    # sun_api = f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}'
    # r = requests.get(sun_api).json()
    r = {
        'results': {
            'sunrise': '10:00:00 AM',
            'sunset': '11:00:00 PM'
        }
    }
    results = r['results']
    sun_rise = time_to_local(results['sunrise'])
    sun_set = time_to_local(results['sunset'])

    current_time = datetime.now()
    midnight = (current_time + timedelta(days=1)).replace(hour=0, minute=0)
    next_update = ((midnight - current_time).seconds) * 1000 # ms until next update after midnight

    window.after(next_update, get_sun_stats) # once per day

    return sun_rise, sun_set
# sleep for 3600 in main loop
# if time between 00:00 and 2:00 grab sun_api
# every hour update weather
# time.sleep(3600)

window = Tk()
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

sun_rise, sun_set = get_sun_stats()


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


sun_stats = ttk.Frame(window)
sun_stats.grid(row=1, column=2)

sunrise = ttk.Label(sun_stats, text=sun_set)
sunrise.grid(row=0, column=1, sticky=N)
sunset = ttk.Label(sun_stats, text=sun_set)
sunrise.grid(row=1, column=1, sticky=N)


window.geometry("800x480")
window.mainloop()