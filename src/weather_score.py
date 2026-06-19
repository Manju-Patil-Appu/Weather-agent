def calculate_weather_score(weather):

    score = 10

    temp = weather["temperature"]
    humidity = weather["humidity"]
    wind = weather["wind_speed"]
    condition = weather["condition"].lower()

    # Temperature impact
    if temp > 38:
        score -= 3
    elif temp > 34:
        score -= 2
    elif temp < 15:
        score -= 2

    # Humidity impact
    if humidity > 90:
        score -= 2
    elif humidity > 80:
        score -= 1

    # Wind impact
    if wind > 10:
        score -= 1

    # Weather impact
    if "rain" in condition:
        score -= 2

    score = max(score, 1)

    return round(score, 1)