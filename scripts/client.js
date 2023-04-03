const WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
const LAT = 42.9849
const LNG = -81.2453
const WINDOW_WIDTH = 800
const WINDOW_HEIGHT = 480

const WEATHER_CODE = {
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

const WEATHER_FORECAST_API = `https://api.open-meteo.com/v1/forecast?latitude=${LAT}&longitude=${LNG}&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,precipitation_sum&timezone=America%2FNew_York`
const CURRENT_WEATHER_API = `https://api.open-meteo.com/v1/forecast?latitude=${LAT}&longitude=${LNG}&current_weather=true&timezone=America%2FNew_York`
const QUOTES_API = 'https://type.fit/api/quotes'

$(document).ready(() => {
    const millisecondsToMidnight = () => {
        let now = new Date()
        let midnight = new Date(now)
        midnight.setHours(24, 0, 0, 0)
        console.log(midnight - now)
    }
    millisecondsToMidnight()

    const currentDate = () => {
        let now = new Date()
        $("#weekday").text(`${WEEKDAYS[now.getDay()]}`)
        $("#month").text(`${MONTHS[now.getMonth()]}`)
        $("#day").text(`${now.getDate()}`)
        $("#year").text(`${now.getFullYear()}`)
        console.log('hello')
        setTimeout(currentDate, 1000)
    }
    currentDate()

    const getCurrentWeather = () => {
        $.ajax(CURRENT_WEATHER_API, { method: 'GET' })
            .then((res) => {
                console.log(res.current_weather)
            })
            .catch((err) => {
                console.log(err)
            })
    }
    getCurrentWeather()

    const getForecast = () => {
        $.ajax(WEATHER_FORECAST_API, { method: 'GET' })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
    }
    getForecast()

    
    const getDailyQuote = () => {
        $.ajax(QUOTES_API, { method: 'GET' })
            .then((res) => {
                data = JSON.parse(res)[0]
                $("#quoteText").text(`${data.text}\n-${data.author}`)
            })
            .catch((err) => {
                console.log(err)
            })
    }
    getDailyQuote()
})

