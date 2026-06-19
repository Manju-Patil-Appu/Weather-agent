def check_alerts(weather):
    alerts = []

    temp = weather["temperature"]
    humidity = weather["humidity"]
    wind_speed = weather["wind_speed"]
    condition = weather["condition"].lower()

    # Rain Alerts
    if "rain" in condition:
        alerts.append(
            "☔ Rain Alert: Rainfall is expected today. Carry an umbrella and allow extra travel time."
        )

    # Heat Alerts
    if temp >= 35:
        alerts.append(
            f"🔥 Heat Alert: Temperature may reach {temp}°C. Stay hydrated and avoid direct sunlight during peak afternoon hours."
        )

    # Strong Wind Alerts
    if wind_speed >= 10:
        alerts.append(
            f"🌪 Wind Alert: Wind speed is {wind_speed} m/s. Be cautious if travelling on two-wheelers."
        )

    # Humidity Alert
    if humidity >= 90:
        alerts.append(
            f"💧 Humidity Alert: Humidity is {humidity}%. Weather may feel significantly hotter than the actual temperature."
        )

    return alerts

