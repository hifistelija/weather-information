import requests
import smtplib

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "********"


# Email credentials
smtp_server = "smtp.mail.yahoo.com"
smtp_port = 587
sender_email = "ilkka.heino27@yahoo.com"
sender_password = "f********"
receiver_email = "********"

# Parameters for OpenWeather API call
parameters = {
    "lat": 60.159088,
    "lon": 24.877670,
    "appid": api_key,
    "units": "metric"
}

# Call OpenWeatherMap API and parse JSON response
response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = response.json()

# Extract temperature and weather type
temperature = data["main"]["temp"]
weather_type = data["weather"][0]["main"]

# Email content
subject = "Current weather information"
body = f"Current temperature is {temperature:.1f} Celsius and the weather is {weather_type}."

# Send email using SMTP
with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
    connection.starttls()
    connection.login(user="ilkka.heino27@yahoo.com", password="fthgnwpidfnahtgk")
    connection.sendmail(
        from_addr="ilkka.heino27@yahoo.com",
        to_addrs="ilkka.heino27@yahoo.com",
        msg=f"Subject: {subject}\n\n{body}"
    )
    connection.close()
