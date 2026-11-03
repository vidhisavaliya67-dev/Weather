import requests

API_KEY = "5b81ce7d63a7c6e5125a835e492e5379"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

City= input("Enter your city name: ")

params = {
    'q': City,
    'appid': API_KEY,
    'units': 'metric'
}   

try:
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        print(f"\n---Weather in {City}.title:---")
        print(f"Temperature: {temperature}°C")      
        print(f"Description: {description}")
        print(f"Humidity: {humidity}%")

    else:
        print("Error: Unable to fetch weather data. Please check the city name and try again.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
        