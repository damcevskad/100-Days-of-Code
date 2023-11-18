import requests
import os
from twilio.rest import Client

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get('STOCK_API_KEY')
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
TWILI0_ACC_SID = os.environ.get('TWILIO_ACC_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

STOCK = "ROST"
COMPANY_NAME = "Ross Stores Inc"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
news_parameters = {
    "q": STOCK,
    "apikey": NEWS_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = response.json()["Time Series (Daily)"]

stock_list = [value for (key, value) in data.items()]
yesterday_price = stock_list[0]["4. close"]
before_yesterday_price = stock_list[1]["4. close"]

difference = float(yesterday_price) - float(before_yesterday_price)
arrow = ""
if difference > 0:
    arrow = "🔺"
else:
    arrow = "🔻"

percentage_difference = round((difference / float(yesterday_price)) * 100)

response2 = requests.get(NEWS_ENDPOINT, params=news_parameters)
articles = response2.json()["articles"][:3]

news = [f"{STOCK}: {arrow} {percentage_difference}% \nHeadline: {articles['title']}. \n Outline: {articles['description']}" for articles in articles]

if abs(percentage_difference) > 5:

    client = Client(TWILI0_ACC_SID, TWILIO_AUTH_TOKEN)
    for article in news:
        message = client.messages \
            .create(body=article, from_='+12512765319', to='+38978283508')
