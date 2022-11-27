import requests
import json
import time

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

    return
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

sunrise = ttk.Label(window, text=sun_rise)
sunrise.grid(row=1, column=2, sticky=N)

window.geometry("800x480")
window.mainloop()