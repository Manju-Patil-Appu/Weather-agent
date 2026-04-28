print("Script started...")

import requests
import smtplib

API_KEY = "0ff9cccd1b71e8605faabe96b626551c"
CITY = "Bangalore"

def get_weather():
    print("Fetching weather...")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    print("API Response:", data)

    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    
    return temp, desc

def generate_advice(temp, desc):
    desc = desc.lower()
    advice = []

    if "rain" in desc:
        advice.append("Carry an umbrella ☔")

    if temp > 32:
        advice.append("Stay hydrated 💧 and avoid heat")

    if temp < 18:
        advice.append("Wear warm clothes 🧥")

    if "cloud" in desc:
        advice.append("Nice calm weather 🌥️")

    if not advice:
        advice.append("Weather looks normal 🙂")

    return "\n".join(advice)

def format_message(temp, desc):
    advice = generate_advice(temp, desc)

    return f"""
Good Morning 🌤️

📍 Weather Report:

🌡️ Temperature: {temp}°C
🌥️ Condition: {desc}

🤖 AI Advice:
{advice}
"""

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def send_email(message):
    EMAIL = "manjupatilappu@gmail.com"
    PASSWORD = "lwhqlluqxlnioucl"

    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = EMAIL
    msg["Subject"] = "Daily Weather Update 🌤️"

    # ✅ Fix encoding here
    msg.attach(MIMEText(message, "plain", "utf-8"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)

    server.sendmail(EMAIL, EMAIL, msg.as_string())
    server.quit()


if __name__ == "__main__":
    temp, desc = get_weather()

    if temp is not None:
        message = format_message(temp, desc)
        send_email(message)
        print("Email sent successfully ✅")