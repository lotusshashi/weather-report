import requests
from pprint import pprint

API_Key="eaa4f3c6621404b4450db778f761ee50"

city=input("Enter Your City :")

base_url="https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data=requests.get(base_url).json()
pprint(weather_data)
