import os
import smtplib

from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_alert_email(weather, alerts):

    if not alerts:
        return

    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    city = weather["city"]

    msg = MIMEMultipart()

    msg["From"] = email
    msg["To"] = email

    first_alert = alerts[0]

    # Dynamic Subject
    if "Rain" in first_alert:
        subject = f"☔ Rain Alert | {city}"

        recommendation = """
Recommended actions:
• Carry an umbrella
• Plan for possible traffic delays
• Avoid leaving electronic devices exposed

Severity: Medium
"""

    elif "Heat" in first_alert:
        subject = f"🔥 Heat Alert | {city}"

        recommendation = """
Recommended actions:
• Stay hydrated
• Avoid direct sunlight during peak afternoon hours
• Take regular breaks if outdoors

Severity: High
"""

    elif "Wind" in first_alert:
        subject = f"🌪 Wind Alert | {city}"

        recommendation = """
Recommended actions:
• Secure loose outdoor items
• Exercise caution while riding two-wheelers
• Monitor local travel advisories

Severity: Medium
"""

    else:
        subject = f"⚠ Weather Alert | {city}"

        recommendation = """
Recommended actions:
• Monitor local weather conditions
• Stay prepared for unexpected changes

Severity: Medium
"""

    msg["Subject"] = subject

    # Dynamic Greeting
    hour = datetime.now().hour

    if hour < 12:
        greeting = "Good Morning"

    elif hour < 17:
        greeting = "Good Afternoon"

    else:
        greeting = "Good Evening"

    body = f"""
{greeting} Manjuu.

A weather condition is not normal today in {city}.

{first_alert}

{recommendation}

Stay safe.

Weather Intelligence Agent
"""

    msg.attach(
        MIMEText(
            body,
            "plain",
            "utf-8"
        )
    )

    server = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )

    server.starttls()

    server.login(
        email,
        password
    )

    server.sendmail(
        email,
        email,
        msg.as_string()
    )

    server.quit()

    print("🚨 Alert email sent")