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

    if forecast_data.get("cod") != "200": #Checks for any api errors, if the code is not 200, there was an error
        print("API Error:", forecast_data.get("message"))
        exit() # Exits the program if there was an API error

    print('\nForecast for Minneapolis: ')
    print("-" * 60 + "\n")

    for forecast in forecast_data['list']: # Each forecast is for a 3 hour period
        timestamp = forecast["dt"]
        readable_time = datetime.fromtimestamp(timestamp)

        temp = forecast['main']['temp'] # The temperature is in the "main" section of the forecast data, and the key for temperature is "temp"
        description = forecast['weather'][0]['description'] 
        windspeed = forecast['wind']['speed']# 
        
        print(f"Time: {readable_time}") 
        print(f"Temp: {temp}°C")  
        print(f"Weather: {description}")
        print(f"Wind Speed: {windspeed} m/s")
        print("-" * 30)
        
    
except Exception as e:
    print(f"An error occurred: {e}")