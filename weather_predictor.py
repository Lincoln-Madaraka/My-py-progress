import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        feels_like = main["feels_like"]
        description = weather["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Description: {description}")
    else:
        print("City not found!")

if __name__ == "__main__":
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    city = input("Enter city name: ")
    get_weather(api_key, city)

