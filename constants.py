WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
LAT = 42.9849
LNG = -81.2453
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 480

WEATHER_CODE = {
    0: 'Clear Sky',
    1: 'Mainly Clear',
    2: 'Partly Cloudy',
    3: 'Overcast',
    45: 'Fog',
    48: 'Depositing Rime Fog',
    51: 'Light Drizzle',
    53: 'Moderate Drizzle',
    55: 'Dense Drizzle',
    56: 'Light Freezing Drizzle',
    57: 'Dense Freezing Drizzle',
    61: 'Slight Rain',
    63: 'Moderate Rain',
    65: 'Heavy Rain',
    66: 'Light Freezing Rain',
    67: 'Heavy Freezing Rain',
    71: 'Slight Snow Fall',
    73: 'Moderate Snow Fall',
    75: 'Heavy Snow Fall',
    77: 'Snow Grains',
    80: 'Slight Rain Showers',
    81: 'Moderate Rain Showers',
    82: 'Heavy Rain Showers',
    85: 'Slight Snow Showers',
    86: 'Heavy Snow Showers'
}

SUN_API = f'https://api.sunrise-sunset.org/json?lat={LAT}&lng={LNG}'
WEATHER_FORECAST_API = f'https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LNG}&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,precipitation_sum&timezone=America%2FNew_York'
CURRENT_WEATHER_API = f'https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LNG}&current_weather=true&timezone=America%2FNew_York'
QUOTES_API = 'https://zenquotes.io/api/today'