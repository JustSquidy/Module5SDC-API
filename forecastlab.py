import os
import requests
from pprint import pprint
from datetime import datetime

# Minneapolis
lat = 44.97
lon = -93.26
units = 'metric'  # change to 'imperial' for quantities in Fahrenheit, miles per hour etc.

api_key = os.environ.get('WEATHER_KEY')  # Set this environment variable on your computer

url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&appid={api_key}'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError if the response code was unsuccessful

    forecast_data = response.json()
    pprint(forecast_data)

    print('Forecast for Minneapolis: ')

    for forecast in forecast_data['list']:
        timestamp = forecast["dt"]
        readable_time = datetime.fromtimestamp(timestamp)

        temp = forecast['main']['temp']
        description = forecast['weather'][0]['description']
        windspeed = forecast['wind']['speed']

        print(f"{readable_time}: {temp}°C, {description}, Wind Speed: {windspeed} m/s")
    

except Exception as e:
    print(f"An error occurred: {e}")