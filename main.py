import requests


weather_service = "https://wttr.in/hhhhhhhh"
weather_service_mirror = "http://wttr.dvmn.org/"
payload = "nTqm&lang=ru"   #"""Параметры сервиса можно посмотреть по ссылке https://wttr.in/:help"""
locations = ("Лондон", "Шереметьево", "Череповец")

def get_url(service: str, location: str) -> str:
    return service + location

def get_response(url: str, payload: str) -> str:
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text

for location in locations:
    try:
       print(get_response(get_url(weather_service, location), payload))
    except requests.exceptions.HTTPError as error:
        print(f"Can't get data from service:\n{error}\nLet's try another one...")
        try:
            print(get_response(get_url(weather_service_mirror, location), payload))
        except requests.exceptions.HTTPError as error:
            exit(f"Can't get data from mirror serice:\n{error}")

