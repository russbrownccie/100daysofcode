import requests
import datetime as dt
from twilio.rest import Client
today = dt.date.today()
yesterday = today - dt.timedelta(days=1)
day_before_yesterday = today - dt.timedelta(days=2)

account_sid = "<snip>"
auth_token = "<snip>"

STOCK_NAME = "BTC"
COMPANY_NAME = "Bitcoin"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "<snip>"
NEWS_API_KEY = "<snip>"

stock_parameters = {
                    "function": "DIGITAL_CURRENCY_DAILY",
                    "symbol": STOCK_NAME,
                    "apikey": STOCK_API_KEY,
                    "market": "USD"
}

news_parameters = {
                    "q": COMPANY_NAME,
                    "sortBy": "relevancy",
                    "apiKey": NEWS_API_KEY,
                    "language": "en",
                    "pageSize": 5,
                    "from": day_before_yesterday,
                    "to": today

}
# alternate variables to test program
# yesterday_close = 34262
# day_before_yesterday_close = 39424

# This gets the stock data - comment this out and comment in above to test a 5% move or greater
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()
nudata = data['Time Series (Digital Currency Daily)']
close_data = [value for (key, value) in nudata.items()]
yesterday_close = float((close_data[1].get('4b. close (USD)')))
day_before_yesterday_close = float((close_data[2].get('4b. close (USD)')))

# This gets the price change, calculates percentage and direction, and if over 5 percent change, gets headlines
price_change = (yesterday_close - day_before_yesterday_close)
if price_change > 0:
    direction = "🔺"
else:
    price_change = abs(price_change)
    direction = "🔻"
percentage = (price_change / yesterday_close) * 100
print(f"Price closed yesterday at {yesterday_close}\nPrice closed day before yesterday at {day_before_yesterday_close}\n"
      f"The price change was {price_change}\nthat's a {percentage} percent change from yesterday")
if percentage > 5:
    list_of_titles = []
    list_of_descriptions = []
    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    data = response.json()
    three_headlines = (data['articles'][0:3])
    for i in range(0, 3):
        list_of_titles.append(three_headlines[i]['title'])
        list_of_descriptions.append(three_headlines[i]['description'])

    firstmessage = f"{STOCK_NAME}: {direction}{int(percentage)}%\n\nHeadline: {list_of_titles[0]}\n\nBrief: {list_of_descriptions[0]}"
    secondmessage = f"{STOCK_NAME}: {direction}{int(percentage)}%\n\nHeadline: {list_of_titles[1]}\n\nBrief: {list_of_descriptions[1]}"
    thirdmessage = f"{STOCK_NAME}: {direction}{int(percentage)}%\n\nHeadline: {list_of_titles[2]}\n\nBrief: {list_of_descriptions[2]}"

#     print(firstmessage)
#     print(secondmessage)
#     print(thirdmessage)

    client = Client(account_sid, auth_token)
    
    message = client.messages \
        .create(
        body=f'{firstmessage}',
        from_='<snip>',
        to='<snip>'
    )
    message = client.messages \
        .create(
        body=f'{secondmessage}',
        from_='<snip>',
        to='<snip>'
    )
    message = client.messages \
        .create(
        body=f'{thirdmessage}',
        from_='<snip>',
        to='<snip>''
    )
    
    print(message.status)
