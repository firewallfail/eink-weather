const WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
const LAT = 42.9849
const LNG = -81.2453
const WINDOW_WIDTH = 800
const WINDOW_HEIGHT = 480

// 10 minute offset for refreshes to ensure api calls don't get stale data
const TIME_OFFSET = 1000 * 60 * 10
const REFRESH_AFTER_ERROR = 1000 * 60 * 5
const MINUTES_15 = 1000 * 60 * 15

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
    const getRandomInt = max => {
        return Math.floor(Math.random() * max);
    }

    const millisecondsToMidnight = () => {
        let now = new Date()
        let midnight = new Date(now)
        midnight.setHours(24, 0, 0, 0)
        return midnight - now + TIME_OFFSET
    }
    millisecondsToMidnight()

    const currentDate = () => {
        let now = new Date()
        $("#weekday").text(`${WEEKDAYS[now.getDay()]}`)
        $("#month").text(`${MONTHS[now.getMonth()]}`)
        $("#day").text(`${now.getDate()}`)
        $("#year").text(`${now.getFullYear()}`)
    }
    currentDate()

    const getCurrentWeather = () => {
        $.ajax(CURRENT_WEATHER_API, { method: 'GET' })
            .then((res) => {
                let weather = res.current_weather
                $("#temp").text(`Temp: ${weather.temperature} \u00B0C`)
                $("#wind").text(`Wind: ${weather.windspeed} km/h`)
                $("#weatherCode").text(`${WEATHER_CODE[weather.weathercode]}`)
                $("#lastRefresh").text(`Refreshed: ${new Date().toLocaleTimeString('en-us', { hour12: false })}`)
                setTimeout(getCurrentWeather, MINUTES_15)
            })
            .catch((err) => {
                console.log(err)
                setTimeout(getCurrentWeather, REFRESH_AFTER_ERROR)
            })
    }
    getCurrentWeather()

    const getForecast = () => {
        currentDate()
        $.ajax(WEATHER_FORECAST_API, { method: 'GET' })
            .then((res) => {
                let forecast = res.daily
                let sunrise = new Date(forecast.sunrise[0]).toLocaleTimeString('en-us', { hour12: false })
                let sunset = new Date(forecast.sunset[0]).toLocaleTimeString('en-us', { hour12: false })
                // today forecast
                $("#todayHigh").text(`High: ${forecast.apparent_temperature_max[0]} \u00B0C`)
                $("#todayLow").text(`Low: ${forecast.apparent_temperature_min[0]} \u00B0C`)
                $("#todayPrecip").text(`Precip: ${forecast.precipitation_sum[0]} mm`)
                $("#todayCode").text(`${WEATHER_CODE[forecast.weathercode[0]]}`)
                // tomorrow forecast
                $("#tomorrowHigh").text(`High: ${forecast.apparent_temperature_max[1]} \u00B0C`)
                $("#tomorrowLow").text(`Low: ${forecast.apparent_temperature_min[1]} \u00B0C`)
                $("#tomorrowPrecip").text(`Precip: ${forecast.precipitation_sum[1]} mm`)
                $("#tomorrowCode").text(`${WEATHER_CODE[forecast.weathercode[1]]}`)
                // sunrise and sunset
                $("#sunRise").text(`Rise: ${sunrise}`)
                $("#sunSet").text(`Set: ${sunset}`)
                // update last refresh
                $("#lastRefresh").text(`Refreshed: ${new Date().toLocaleTimeString('en-us', { hour12: false })}`)
                setTimeout(getForecast, millisecondsToMidnight())
            })
            .catch((err) => {
                console.log(err)
                setTimeout(getForecast, REFRESH_AFTER_ERROR)
            })
    }
    getForecast()

    
    const getDailyQuote = () => {
        $.ajax(QUOTES_API, { method: 'GET' })
            .then((res) => {
                let data = JSON.parse(res)
                let dataLength = data.length
                let quote = ''
                for (i in data) {
                    let randomInt = getRandomInt(dataLength)
                    quote = `${data[randomInt].text}\n-${data[randomInt].author}`
                    if (quote.length < 120) {
                        break
                    } else {
                        quote = 'All quotes too long'
                    }
                }
                $("#quoteText").text(`${quote}`)
                setTimeout(getDailyQuote, millisecondsToMidnight())
            })
            .catch((err) => {
                console.log(err)
                setTimeout(getDailyQuote, REFRESH_AFTER_ERROR)
            })
    }
    getDailyQuote()
})

