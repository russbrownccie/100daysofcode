import requests
from datetime import datetime
import os
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
NUTRITION_URL = os.environ.get("NUTRITION_URL")
SHEET_ENDPOINT= os.environ.get("SHEET_ENDPOINT")
TOKEN = os.environ.get("TOKEN")

params = {
    "query":input("Tell me what exercises you did: "),
    "gender": "male",
    "weight_kg": <snip>,
    "height_cm": <snip>,
    "age": <snip>
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=NUTRITION_URL, json=params, headers=headers)
response.raise_for_status()
data = response.json()
now = datetime.now()

for item in range (0, (len(data['exercises']))):

    Name = (data['exercises'][item]['name'])
    Calories = (data['exercises'][item]['nf_calories'])
    Duration = (data['exercises'][item]['duration_min'])

    data_submitted = {
        "workout": {
            "date": now.strftime('%d/%m/%Y'),
            "time": now.strftime('%X'),
            "exercise": Name.title(),
            "duration": Duration,
            "calories": Calories
        }
    }
    sheety_header = {
        "Authorization": TOKEN
    }
    requests.post(url=SHEET_ENDPOINT, json=data_submitted, headers=sheety_header)
    print(f"you did {Name} for {Duration} and burned {Calories} calories on {now.strftime('%d/%m/%Y')} at {now.strftime('%X')} ")
