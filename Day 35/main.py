import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import datetime as dt
import random
import smtplib
#Quote program and info
my_email = "xxxxxxxx"
my_password = os.environ.get("MY_PASSWORD")
quotes = []
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as file:
        quotes = file.readlines()

    inspirational_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="xxxxx",
            msg=f"Subject:Inspirational Quote\n\n{inspirational_quote}"
        )

# weather part of program
api_key = os.environ.get("OWM_API_KEY")
MY_LAT=xxxx
MY_LONG=-xxxx
account_sid = "xxxxx"
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
            "lat": xxxx,
            "lon": xxxx,
            "appid": "7047845544fdb9858e495a7cf3fa81c9",
            "units": "imperial",
            "exclude": "current,minutely,daily"
            }

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
print (response.status_code)
response.raise_for_status()
data = response.json()

# my version of cycling thru data
# for hours in range (0,12):
#     is_it_raining = (data['hourly'][hours]['weather'][0]['id'])
#     if is_it_raining <700:
#         print("Need an Umbrella")
#         break

weather_slice = data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code =(hour_data["weather"][0]['id'])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain, bring an umbrella",
        from_='+15672292135',
        to='+xxxxxx'
    )

    print(message.status)
