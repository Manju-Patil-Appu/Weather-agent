import os
import requests


def get_weather():
    api_key = os.getenv("API_KEY")
    city = os.getenv("CITY")

    if not api_key:
        raise ValueError("API_KEY not found in environment variables")

    if not city:
        raise ValueError("CITY not found in environment variables")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        raise Exception(
            f"Weather API Error: {response.status_code} - {response.text}"
        )

    data = response.json()

    weather_data = {
        "city": data["name"],
        "temperature": round(data["main"]["temp"], 1),
        "feels_like": round(data["main"]["feels_like"], 1),
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "condition": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"],
        "country": data["sys"]["country"]
    }

    return weather_data