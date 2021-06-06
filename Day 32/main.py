from pandas import *
import datetime as dt
import random
import smtplib
MY_MAIL = "xxxxx"
MY_PASSWORD = "xxxxxx"
now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv('birthdays.csv')



birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]

    choice = random.randint(1,3)
    with open (f"letter_templates/letter_{choice}.txt") as letter_file:
        contents = letter_file.read()
        new_contents = contents.replace(f"[NAME]", birthday_person["name"])


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_MAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{new_contents}")
