import requests
from twilio.rest import Client

# OpenWeatherMap API endpoint and API key
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "65fe3d17fbf436110de633f7c1b5f989"

# Twilio API credentials
account_sid = "your_account_sid_here"
auth_token = "your_auth_token_here"
twilio_phone_number = "your_twilio_phone_number_here"
my_phone_number = "your_phone_number_here"

# Parameters for OpenWeatherMap API call
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

# Send an SMS using Twilio API
client = Client(account_sid, auth_token)
message = client.messages.create(
    body=f"Current temperature is {temperature:.1f} Celsius and the weather type is {weather_type}.",
    from_=twilio_phone_number,
    to=my_phone_number
)
print(f"SMS sent: {message.sid}")
