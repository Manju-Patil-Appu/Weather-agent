import json
import os
from datetime import datetime

HISTORY_FILE = "data/weather_history.json"


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_weather(weather):
    history = load_history()

    record = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "temperature": weather["temperature"],
        "humidity": weather["humidity"],
        "condition": weather["condition"]
    }

    # Avoid duplicate entries for same day
    history = [
        item for item in history
        if item["date"] != record["date"]
    ]

    history.append(record)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def get_yesterday():
    history = load_history()

    if len(history) < 2:
        return None

    history.sort(key=lambda x: x["date"])

    return history[-2]