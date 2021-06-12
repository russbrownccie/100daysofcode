import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "snip"
TOKEN = snip
GRAPHS_ID = "graph1"
# date = datetime.now()
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
#
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config ={
#     "id": "graph1",
#     "name": "Minutes Read Per Day",
#     "unit": "Minutes",
#     "type": "int",
#     "color": "sora"
# }

headers = {
    "X-USER-TOKEN": TOKEN
}
date = datetime(year=2021, month=6, day=8)
newdata_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHS_ID}"

data_params = {
    "date": date.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you read today? ")
}

response = requests.post(url=newdata_endpoint, json=data_params, headers=headers)
print (response.text)
#
# print(date.strftime("%Y%m%d"),)

# update_params = {
#     "quantity": "45"
# }
#
# update_endpoint = f"{newdata_endpoint}/20210609"
#
# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)
