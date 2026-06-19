import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(report, weather):

    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    if not email:
        raise ValueError("EMAIL not found in .env")

    if not password:
        raise ValueError("PASSWORD not found in .env")

    msg = MIMEMultipart()

    msg["From"] = email
    msg["To"] = email

    city = weather["city"]
    temp = weather["temperature"]

    msg["Subject"] = (
    f"🌤 Morning Briefing | {city} | {temp}°C"
)

    msg.attach(
        MIMEText(
            report,
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

    print("✅ Email sent successfully")