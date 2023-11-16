# Day 35

import requests
from twilio.rest import Client
import os

api_endpoint = "https://api.openweathermap.org/data/2.8/onecall"
key = os.environ.get("API_KEY")
account_sid = "AC3bb607b027479977005192816e9f47ce"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 41.997345,
    "lon": 21.427996,
    "appid": key,
    "exclude": "current,minutely,daily"
}

response = requests.get(api_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

hour = 0
will_rain = False
while hour < 12:
    weather_id = weather_data["hourly"][hour]["weather"][0]["id"]
    weather_desc = weather_data["hourly"][hour]["weather"][0]["description"]
    if weather_id < 700:
        will_rain = True
        # print(weather_desc + " at " + str(hour) + ":00 ")
    hour += 1

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Rainy day ahead ☔️",
        from_='+12512765319',
        to='+38978283508'
    )

    print(message.status)
