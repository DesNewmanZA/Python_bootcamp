# Import needed modules
import requests
from twilio.rest import Client
from datetime import date, timedelta

# Define constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_API_KEY = "QXIHSATYWNBOA4UU"
PRICE_CHANGE_THRESHOLD = 0.5
NEWS_API_KEY = "aea2995d29fd472dbd1a57981ab2d40a"
account_sid = 'AC89e6c92df93440cc709dd561508007ed'
auth_token = 'c42b2aaae2b0e36dcf4359c7f2665e36'
my_number = 'masked_number'

# Define get news function
def get_news():
    news_response = requests.get(url=f"https://newsapi.org/v2/everything?q={STOCK}&apiKey={NEWS_API_KEY}")
    news_response.raise_for_status()
    titles = news_response.json()['articles'][0]['title']
    return titles


def send_notification(relative_difference, news_title):
    client = Client(account_sid, auth_token)
    if relative_difference > 0:
        message = f"{STOCK}: 🔺 {relative_difference}%\nHeadline: {news_title}"
    else:
        message = f"{STOCK}: 🔻 {relative_difference}%\nHeadline: {news_title}"
    SMS = client.messages.create(
        body=message,
        from_="+18545045401",
        to=my_number,
    )
    return message


# Get required dates for the work
today = date.today()
yesterday = str(today + timedelta(days=-1))
two_days_ago = str(today + timedelta(days=-2))

# Pull stock prices from API - when price changes 5% day-on-day, print "get news"
response = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHA_VANTAGE_API_KEY}")
response.raise_for_status()
data = response.json()['Time Series (Daily)']
price_yesterday = float(data[yesterday]['4. close'])
price_two_days_ago = float(data[two_days_ago]['4. close'])
relative_difference = (price_yesterday/price_two_days_ago - 1) * 100

# If relative difference is above the threshold, get the latest news and send a notification
if relative_difference > PRICE_CHANGE_THRESHOLD or relative_difference < -PRICE_CHANGE_THRESHOLD:
    news_title = get_news()
    msg = send_notification(relative_difference, news_title)
