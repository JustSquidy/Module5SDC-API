import requests
import os
from datetime import datetime
from pprint import pprint

try:
    key = os.environ.get("WEATHER_KEY")
    query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': key}

    url = 'https://api.openweathermap.org/data/2.5/forecast'

    data = requests.get(url, params=query).json()

    pprint(data)

except Exception as e:
    print(f"An error occurred: {e}")