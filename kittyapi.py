import requests


try:
    response = requests.get("https://catfact.ninja/fact")
    print(response.status_code)

    response.raise_for_status()  
    print(response.text)
    print(response.json())

    data = response.json()
    fact = data["fact"]
    print(f"Fact: {fact}")

except Exception as e:
    print(f"An error occurred: {e}")