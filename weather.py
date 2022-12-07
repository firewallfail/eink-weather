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


def time_to_midnight():
    current_time = datetime.now()
    midnight = (current_time + timedelta(days=1)).replace(hour=0, minute=0)
    return ((midnight - current_time).seconds) * 1000 # ms until next update after midnight


def draw_sun_stats(next_update, sun_rise, sun_set):
    sun_stats = ttk.Frame(window)
    sun_stats.grid(row=1, column=2)

    sunrise = ttk.Label(sun_stats, text=f'Sun Rise: {sun_rise}')
    sunrise.grid(row=0, column=1, sticky=N)
    sunset = ttk.Label(sun_stats, text=f'Sun Set: {sun_set}')
    sunset.grid(row=1, column=1, sticky=N)

    window.after(next_update, get_sun_stats) # once per day


def get_sun_stats():
    results = requests.get(CONS.SUN_API).json().get('results', None)

    if not results:
        thirty_mins_in_ms = 30 * 60 * 1000
        draw_sun_stats(thirty_mins_in_ms, 'Error', 'Other Error')
        return False

    sun_rise = time_to_local(results['sunrise'])
    sun_set = time_to_local(results['sunset'])

    next_update = time_to_midnight()
    draw_sun_stats(next_update, sun_rise, sun_set)


def get_date_stats():
    date = {
        'weekday': CONS.WEEKDAYS[datetime.today().weekday()],
        'month': CONS.MONTHS[datetime.today().month - 1],
        'day': datetime.today().day,
        'year': datetime.today().year
    }
    next_update = time_to_midnight()
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


def get_weather_forecast():
    results = requests.get(CONS.WEATHER_FORECAST_API).json().get('daily', None)
    today_forecast = {
        'temp_high': results.get('temperature_2m_max')[0],
        'temp_low': results.get('temperature_2m_min')[0],
        'precip_sum': results.get('precipitation_sum')[0],
        'weather_code': results.get('weathercode')[0]
    }
    tomorrow_forecast = {
        'temp_high': results.get('temperature_2m_max')[1],
        'temp_low': results.get('temperature_2m_min')[1],
        'precip_sum': results.get('precipitation_sum')[1],
        'weather_code': results.get('weathercode')[1]
    }
    next_update = time_to_midnight()
    draw_forecast_tiles(next_update, today_forecast, tomorrow_forecast)


def draw_forecast_tiles(next_update, today_forecast, tomorrow_forecast):
    forecasts = (today_forecast, tomorrow_forecast)
    titles = ('Today Forecast', 'Tomorrow Forecast')
    for i in range(2):
        draw_forecast_tile(forecasts[i], i+1, titles[i])
    window.after(next_update, get_weather_forecast) # once per day


def draw_forecast_tile(forecast, column, text):
    forecast_tile = ttk.Frame(window)
    forecast_tile.grid(row=0, column=column)

    title = ttk.Label(forecast_tile, text=text)
    title.grid(row=0, column=0)

    temp_high = ttk.Label(forecast_tile, text=f"High: {forecast['temp_high']}°C")
    temp_high.grid(row=1, column=0)

    temp_low = ttk.Label(forecast_tile, text=f"Low: {forecast['temp_low']}°C")
    temp_low.grid(row=2, column=0)

    precip_sum = ttk.Label(forecast_tile, text=f"Precip: {forecast['precip_sum']}mm")
    precip_sum.grid(row=3, column=0)

    weather_code = ttk.Label(forecast_tile, text=f"{CONS.WEATHER_CODE[forecast['weather_code']]}")
    weather_code.grid(row=4, column=0)


def get_current_weather():
    results = requests.get(CONS.CURRENT_WEATHER_API).json().get('current_weather', None)
    draw_current_weather_tile(results)



def draw_current_weather_tile(current_weather):
    current_weather_tile = ttk.Frame(window)
    current_weather_tile.grid(row=0, column=0)

    title = ttk.Label(current_weather_tile, text='Current Weather')
    title.grid(row=0, column=0)

    temp = ttk.Label(current_weather_tile, text=f"Temp: {current_weather['temperature']}°C")
    temp.grid(row=1, column=0)

    wind = ttk.Label(current_weather_tile, text=f"Wind: {current_weather['windspeed']}Km/h")
    wind.grid(row=2, column=0)

    weather_code = ttk.Label(current_weather_tile, text=f"{CONS.WEATHER_CODE[current_weather['weathercode']]}")
    weather_code.grid(row=3, column=0)

    half_hour = 30 * 60 * 1000
    window.after(half_hour, get_current_weather)


def get_quote():
    results = requests.get(CONS.QUOTES_API).json()[0]
    draw_quote_tile(results)


def draw_quote_tile(quote):
    quote_tile = ttk.Frame(window)
    
    quote_tile.rowconfigure(0, weight=2)
    quote_tile.rowconfigure(1, weight=5)
    quote_tile.grid(row=1, column=1)

    title = ttk.Label(quote_tile, text='Quote')
    title.grid(row=0, column=0)

    quote = ttk.Label(quote_tile, text=f"{quote['q']}\n-{quote['a']}", wraplength=240)
    quote.grid(row=1, column=0)


    next_update = time_to_midnight()
    window.after(next_update, get_quote)
    
      
window = Tk()
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
get_current_weather()
get_weather_forecast()
get_date_stats()
get_quote()
get_sun_stats()

window.geometry("800x480")
window.mainloop()
