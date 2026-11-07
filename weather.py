import os

from dotenv import load_dotenv
from requests import get

# Инициализация окружения
load_dotenv()
api_key = os.getenv('API_KEY')

city = input('Type the city: ')

# Запрос координат
geo_response = get(f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}")
geo_info = geo_response.json()

if not geo_info:
    print("City not found!")
    exit()

lat = geo_info[0]['lat']
lon = geo_info[0]['lon']

# Запрос погоды
weather_response = get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric")
weather_data = weather_response.json()

temp = weather_data['main']['temp']
feels_like = weather_data['main']['feels_like']
conditions = weather_data['weather'][0]['main']

print("-" * 30)
print(f'Temperature: {round(temp)} {conditions}')
print(f'Feels like: {round(feels_like)}')
print("-" * 30)
