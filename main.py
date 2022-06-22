import requests


def main():
    weather_service = "https://wttr.in/"
    payload = {"lang": "ru", "nTqm": ""}
    locations = ("Лондон", "Шереметьево", "Череповец")

    for location in locations:
        try:
            url = f"{weather_service}{location}"
            response = requests.get(url, params=payload)
            response.raise_for_status()
            print(response.text)
        except requests.exceptions.HTTPError as error:
            print(f"Can't get data from service:\n{error}")

if __name__ == '__main__':
    main()