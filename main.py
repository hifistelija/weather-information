import requests
import smtplib

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "65fe3d17fbf436110de633f7c1b5f989"


# Email credentials
smtp_server = "smtp.mail.yahoo.com"
smtp_port = 587
sender_email = "******"
sender_password = "******"
receiver_email = "******"

# Parameters for OpenWeather API call
parameters = {
    "lat": 60.159088,
    "lon": 24.877670,
    "appid": api_key,
    "units": "metric"
}

# Call OpenWeatherMap API and parse JSON response
response = requests.get(OWN_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

# Extract temperature and weather type
temperature = data["main"]["temp"]
weather_type = data["weather"][0]["main"]

# Email content
subject = "Current weather information"
body = f"Current temperature is {temperature:.1f} Celsius and the weather is {weather_type}."

# Send email using SMTP
with smtplib.SMTP(smtp_server, smtp_port) as connection:
    connection.starttls()
    connection.login(user=sender_email, password=sender_password)
    connection.sendmail(from_addr=sender_email, to_addrs=receiver_email,
                        msg=f"Subject: {subject}\n\n{body}")
    connection.close()
