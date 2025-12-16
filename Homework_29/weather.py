import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str) -> str:
    """Fetch current weather for a given city"""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "uk"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]

        logging.info(f"Weather request success for city={city}")
        return f"Погода в {city}: {temp:+.0f}°C, {description}"

    except requests.exceptions.RequestException as e:
        logging.error(f"Weather request failed for city={city}: {e}")
        return "Не вдалося отримати дані про погоду. Спробуйте пізніше."
