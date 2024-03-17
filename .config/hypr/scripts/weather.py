#!/usr/bin/env python

import json
import requests

# OpenWeather API key (replace with your own API key)
api_key = "25a376cb5b9e5550fe6f53290a62c8cc"

# OpenWeather API endpoint for current weather
api_endpoint = "https://api.openweathermap.org/data/2.5/weather"

# City ID for your location (replace with the correct city ID)
city_id = "792680"

# Weather icons
weather_icons = {
    "01d": "☀️", #clear day
    "01n": "🌙", #clear night
    "02d": "🌤️", #partly cloudy day
    "02n": "☁️", #partly cloudy night
    "03d": "☁️", #cloudy day
    "03n": "☁️", #cloudy night
    "04d": "☁️", #overcast day
    "04n": "☁️", #overcast night
    "09d": "🌦️", #rain day
    "09n": "🌧️", #rain night
    "10d": "🌦️", #rain showers day
    "10n": "🌧️", #rain showers night
    "11d": "⛈️", #thunderstorm day
    "11n": "⛈️", #thunderstorm night
    "13d": "🌨️☃️", #snow day
    "13n": "🌨️☃️", #snow night
    "50d": "🌫️", #fog day
    "50n": "🌫️", #fog night
}

# API request parameters
params = {
    "id": 792680,
    "appid": "25a376cb5b9e5550fe6f53290a62c8cc",
    "units": "metric",  # Use "imperial" for Fahrenheit
}

# Make the API request
response = requests.get(api_endpoint, params=params)
data = response.json()

# Current temperature
temp = data["main"]["temp"]
formatted_temp = "{:.1f}".format(temp)

# Current status phrase
status = data["weather"][0]["description"]
status = f"{status[:16]}.." if len(status) > 17 else status

# Weather icon
icon_code = data["weather"][0]["icon"]
icon = weather_icons.get(icon_code, weather_icons["03d"])

# Temperature feels like
temp_feel = data["main"]["feels_like"]
formatted_feel_temp = "{:.1f}".format(temp_feel)
temp_feel_text = f"Feels like {formatted_feel_temp}°C"

# Min-max temperature
temp_min = data["main"]["temp_min"]
temp_max = data["main"]["temp_max"]
formatted_temp_min = "{:.1f}".format(temp_min)
formatted_temp_max = "{:.1f}".format(temp_max)
temp_min_max = f"  {formatted_temp_min}\t\t  {formatted_temp_max}"

# Wind speed
wind_speed = data["wind"]["speed"]
wind_text = f"  {wind_speed} m/s"

# Humidity
humidity = data["main"]["humidity"]
humidity_text = f"  {humidity}%"

# Visibility
visibility = data.get("visibility")
visibility_text = f"  {visibility} meters" if visibility is not None else "N/A"

# Air quality index (N/A in this example, you may need a separate API for this)
air_quality_index = "N/A"

# Hourly rain prediction (N/A in this example, you may need a separate API for this)
prediction = ""

# Tooltip text
tooltip_text = str.format(
    "\t\t{}\t\t\n{}\n{}\n{}\n\n{}\n{}",
    f'<span size="xx-large">{formatted_temp}°C</span>',
    f"<big>{icon}</big>",
    f"<big>{status}</big>",
    f"<small>{temp_feel_text}</small>",
    f"<big>{temp_min_max}</big>",
    f"{wind_text}\t\t{humidity_text}",
)

# Print waybar module data
out_data = {
    "text": f"{icon} {formatted_temp}°C",
    "alt": status,
    "tooltip": tooltip_text,
    "class": icon_code,
}
print(json.dumps(out_data))