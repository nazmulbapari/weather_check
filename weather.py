import requests
from pprint import pprint

API_Key = '3a8659cb947525fc937cd21961c4a66c'

city = input("Enter a city:")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)