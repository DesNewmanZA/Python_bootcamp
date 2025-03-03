# Import needed modules
from bs4 import BeautifulSoup
import requests
import smtplib

# Define global variables
# Sticking to the static page - it's not the best idea to scrape Amazon
target_price = 100
url = "https://appbrewery.github.io/instant_pot/"

# Scrape website
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

# Extract current price
price = float(soup.find(class_='a-offscreen').text.replace('$', ''))

# Extract product name
prod_name = " ".join(soup.find(id="productTitle").text.split()).split(',')[0]


# Define function that sends email if price is below target price
def price_check_mail(curr_price, target_price, prod_name, url):
    if curr_price < target_price:
        return f"{prod_name} is now on sale for ${curr_price}! {url}"
        # NOT GOING TO EMAIL OUT - PRINCIPLE REMAINS
        # with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        #     connection.starttls()
        #     result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        #     connection.sendmail(
        #         from_addr=YOUR_EMAIL,
        #         to_addrs=YOUR_EMAIL,
        #         msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        #     )
    else:
        pass


print(price_check_mail(90, target_price, prod_name, url))