import requests
import datetime
from twilio.rest import Client

account_sid = "AC8700906"
auth_token = "2849a6ac1"
tesla_stock_api_key = "UF"
news_api_key="a580"

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&interval=60min&apikey={tesla_stock_api_key}'
r = requests.get(url)
data = r.json()

yesterday = str((datetime.datetime.today() - datetime.timedelta(days=1)).date())
past_open_stock_price= float(data['Time Series (Daily)'][yesterday]['1. open'])
past_close_stock_price= float(data['Time Series (Daily)'][yesterday]['4. close'])

stock_return = round(((past_close_stock_price - past_open_stock_price)/past_open_stock_price)*100, 2)

if stock_return < 0:
    stock_return = str(stock_return)+"%"+ "🔻(loss)"
else:
    stock_return = str(stock_return) + "%" + "🔺(gain)"

response = requests.get(f"https://newsapi.org/v2/everything?q=tesla&from=2022-12-24&sortBy=publishedAt&apiKey={news_api_key}").json()
data = response['articles'][0]
published_at = data['publishedAt']
news_title = data['title']
news_description = data['url']

news_outlet = f"\n\n{published_at}\nnew title: \n{news_title}\nnews link: \n{news_description}"

client = Client(account_sid, auth_token)

message = client.messages.create(
                              messaging_service_sid='fbc55941',
                              body=f"Date: {yesterday}\nTesla Stock Open: {past_open_stock_price}\nTesla Stock Close: {past_close_stock_price}\nTotal Return: {stock_return}\n{news_outlet}.",
                              to='+91864'
                          )

print(message.status)

