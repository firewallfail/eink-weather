import requests
import json
import time
import datetime

from tkinter import *
from tkinter import ttk




def get_sun_stats():
    lat = 42.984924
    lng = -81.245277
    sun_api = f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}'
    r = requests.get(sun_api).json()
    results = r['results']
    sun_rise = results['sunrise']
    sun_set = results['sunset']

    current_time = datetime.datetime.now()
    midnight = (current_time + datetime.timedelta(days=1)).replace(hour=0, minute=0)
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


sun_stats = ttk.Label(window, text="Rise and set")
sun_stats.rowconfigure(0, weight=1)
sun_stats.rowconfigure(1, weight=1)
sun_stats.columnconfigure(0, weight=1)
sun_stats.columnconfigure(1, weight=1)
sun_stats.columnconfigure(2, weight=1)
sun_stats.grid(row=1, column=2, sticky=N)

sunrise = ttk.Label(sun_stats, text=sun_set)
sunrise.grid(row=1, column=1, sticky=N)
sunset = ttk.Label(sun_stats, text=sun_set)
sunrise.grid(row=1, column=1, sticky=N)


window.geometry("800x480")
window.mainloop()