import requests
import json
import os
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

# Get city input
city = input("Enter the name of the city: \n")

# Your WeatherAPI URL with city
url = f"http://api.weatherapi.com/v1/current.json?key=7e0affe4b84746ab98a123035250105&q={city}&api=yes"

# Make request
r = requests.get(url)

# Parse JSON response
weather_data = json.loads(r.text)

# Extract temperature
temp_c = weather_data['current']['temp_c']
condition = weather_data['current']['condition']['text']

# Print and speak the result
weather_report = f"The current temperature in {city} is {temp_c} degrees Celsius with {condition}."
print(weather_report)

engine.say(weather_report)
engine.runAndWait()
