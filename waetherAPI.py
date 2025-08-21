import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%t+%C"
    response = requests.get(url)
    return response.text if response.status_code == 200 else "Error!"




if __name__ == "__main__":
    city = input("Enter city name: ")
    print("Weather:", get_weather(city))
