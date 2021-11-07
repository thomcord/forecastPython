import requests
from pprint import pprint
import json
import pandas as pd

print("Welcome to the daily Forecast application. Here you can find the Weather conditions for your desired location")
api_key = "95999815cb87bf974f83ba4f5cba8d94"

city = input("Enter the city desired: ")
base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city+""
weather_data = requests.get(base_url).json()

pprint(weather_data)

'''
def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city+""
    weather_data = requests.get(base_url).json()
    return weather_data
get_weather (city)
'''



