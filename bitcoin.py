import requests
from pprint import pprint

try:
    response = requests.get("https://claraj.github.io/mock-bitcoin/currentprice.json")
    data = response.json()
    pprint(data)

    dollar_exchange_rate = data["bpi"]["USD"]["rate"]
    print(f"Current Bitcoin price in USD: {dollar_exchange_rate}")

    bitcoin = float(input("Enter the amount of Bitcoin you want to convert to USD: "))

    total_usd_value = bitcoin * float(dollar_exchange_rate)

    print(f"{bitcoin} Bitcoin is equivalent to ${total_usd_value:.2f} USD.")

except Exception as e:
    print(f"An error occurred: {e}")