from src.history_service import get_yesterday
from src.context_engine import get_user_context


def generate_insight(weather):

    city = weather["city"]
    temp = weather["temperature"]
    feels_like = weather["feels_like"]
    humidity = weather["humidity"]
    condition = weather["condition"].lower()
    user = get_user_context()
    name = user["name"]

    insight = []

    # Opening Summary
    insight.append(
    f"Good morning {name}.\n\n{city} is experiencing {condition} today."
)

    # Temperature Analysis
    if temp >= 35:
        insight.append(
            f"The current temperature is {temp}°C, which is significantly above comfortable levels. Outdoor exposure should be minimized during afternoon hours."
        )

    elif temp >= 30:
        insight.append(
            f"The temperature is {temp}°C, resulting in warm conditions throughout the day."
        )

    elif temp >= 22:
        insight.append(
            f"The current temperature is {temp}°C, providing generally comfortable conditions for daily activities."
        )

    else:
        insight.append(
            f"The temperature is {temp}°C, making today relatively cool."
        )

    # Feels Like Analysis
    if feels_like - temp >= 2:
        insight.append(
            f"Due to humidity and atmospheric conditions, it may feel closer to {feels_like}°C."
        )

    # Humidity Analysis
    if humidity >= 85:
        insight.append(
            "Humidity levels are very high, which may lead to discomfort despite moderate temperatures."
        )

    elif humidity >= 70:
        insight.append(
            "Humidity is elevated and may make conditions feel warmer than expected."
        )

    elif humidity >= 50:
        insight.append(
            "Humidity levels remain within a moderate range."
        )

    # Weather Condition Analysis
    if "rain" in condition:
        insight.append(
            "Rainfall is expected, so carrying an umbrella is recommended."
        )

    elif "cloud" in condition:
        insight.append(
            "Cloud cover should help reduce direct heat exposure during the day."
        )

    elif "clear" in condition:
        insight.append(
            "Clear skies are expected, providing excellent visibility."
        )

    # Historical Comparison
    yesterday = get_yesterday()

    if yesterday:

        diff = round(temp - yesterday["temperature"], 1)

        if diff > 0:
            insight.append(
                f"Compared to yesterday, temperatures are higher by {diff}°C."
            )

        elif diff < 0:
            insight.append(
                f"Compared to yesterday, temperatures are lower by {abs(diff)}°C."
            )

        else:
            insight.append(
                "Temperature levels remain unchanged compared to yesterday."
            )

    # Closing Summary
    insight.append(
        "No significant weather disruptions are expected based on current conditions."
    )

    return "\n\n".join(insight)