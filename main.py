from dotenv import load_dotenv

from src.weather_service import get_weather
from src.intelligence_engine import generate_insight
from src.alert_engine import check_alerts
from src.report_generator import generate_report
from src.history_service import save_weather
from src.email_service import send_email
from src.alert_email_service import send_alert_email

load_dotenv()

weather = get_weather()

save_weather(weather)

insight = generate_insight(weather)

alerts = check_alerts(weather)

send_alert_email(weather, alerts)

report = generate_report(
    weather,
    insight,
    alerts
)

print(report)

send_email(report, weather)  