

import datetime as dt
import random
import smtplib
my_email = "xxxxxxxxx@gmail.com"
my_password = "xxxxxxx"
quotes = []
now = dt.datetime.now()
day_of_week = now.weekday()


if day_of_week == 3:
    with open("quotes.txt") as file:
        quotes = file.readlines()

    inspirational_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="xxxxxxxx@yahoo.com",
            msg=f"Subject:Inspirational Quote\n\n{inspirational_quote}"
        )

