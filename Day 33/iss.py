import requests
from datetime import datetime
import smtplib
import time
while True:
    time.sleep(60)

    MY_LAT = xxxxxx
    MY_LONG = xxxxxx
    is_overhead = False
    is_nighttime = False
    MY_EMAIL = "xxxxxx@gmail.com"
    MY_PASSWORD = "xxxxxxx"

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT-5) < iss_latitude < (MY_LAT+5) and (MY_LONG-5) < iss_longitude < (MY_LONG +5):
        is_overhead = True
    else:
        is_overhead = False


    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    sunrise -= 8
    sunset -= 8
    if sunrise < 0:
        sunrise += 24
    if sunset < 0:
        sunset +=24
        
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        is_nighttime = True
    else:
        is_nighttime = False



    print(is_overhead)
    print(time_now.hour)

    if is_nighttime and is_overhead:

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.startttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="xxxxxxxx",
                msg=f"Subject:ISS is overhead\n\nThe ISS is overhead at {iss_latitude} Latitude and {iss_longitude} "
                    f"Longitude at {time_now}"
            )
            )


