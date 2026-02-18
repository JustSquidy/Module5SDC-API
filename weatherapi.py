import requests
import os 
from pprint import pprint

try:
    system_var = os.environ.get("WEATHER_KEY")
    # print(f"API Key: {system_var}")

    city = input("Enter the city name: ")
    country = input("Enter the country code (For ex: us for United States): ")
    standard = input("Enter the unit of measurement (imperial for Fahrenheit, metric for Celsius): ")

    temp_unit = "°F" if standard == "imperial" else "°C"

    # url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&units={standard}&appid={system_var}" 
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {"q": f"{city},{country}", "units": standard, "appid": system_var}

    data = requests.get(url, params=params).json()
    pprint(data)

    temp = data["main"]["temp"]
    print(f"The current temperature in {city} is {temp}{temp_unit}.")

except Exception as e:
    print(f"An error occurred: {e}")