'''Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan
säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi.
Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
 Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.'''

import requests


api_key = "5757ecb8f231d7f35b475bee9fb12589"

city_name= input("Please enter city name")

request= {}

request= f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

try:
    response_content = requests.get(request).json()
    #print(response_content)
    print(response_content["weather"][0]["description"])
    kelvins = response_content["main"]["temp"]
    celsius = kelvins -273.15
    print(round(celsius, 2))
except:
    print(error)