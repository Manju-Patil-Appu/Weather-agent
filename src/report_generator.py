from src.weather_score import calculate_weather_score



def generate_report(weather, insight, alerts):
    score = calculate_weather_score(weather)
    city = weather["city"]

    report = f"""
    


🌤 Weather Intelligence Report

📍 Location: {city}

🌡 Temperature: {weather['temperature']}°C
🤗 Feels Like: {weather['feels_like']}°C
💧 Humidity: {weather['humidity']}%
🌬 Wind Speed: {weather['wind_speed']} m/s
☁ Condition: {weather['condition']}
⭐ Weather Score: {score}/10

🧠 AI Weather Insight

{insight}

⚠ Weather Alerts
"""

    if alerts:
        report += "\n".join(alerts)

    else:
        report += "\n✅ No weather alerts today."

    return report