# Import needed modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Open up an instance of the web browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://appbrewery.github.io/Zillow-Clone/")


# Define function to clean up price strings
def clean_string(my_str):
    my_str = my_str.replace('$', '')
    my_str = my_str.replace('/mo', '')
    my_str = my_str.replace(',', '')
    my_str = my_str.replace('+', '')
    my_str = my_str.replace('1 bd', '')
    my_str = my_str.replace('1bd', '')
    my_str = my_str.strip()
    return my_str


# Find all prices, addresses and URLs - NB. all the same number of elements
raw_prices = driver.find_elements(By.CSS_SELECTOR, "[data-test='property-card-price']")
raw_address = driver.find_elements(By.CSS_SELECTOR, "[data-test='property-card-addr']")
raw_URLs = driver.find_elements(By.CLASS_NAME, "property-card-link")

# Clean up information and output into a CSV file
results = pd.DataFrame(columns=['Address', 'Price', 'URL'])
for (price, address, url) in zip(raw_prices, raw_address, raw_URLs):
    # Clean up information
    price = clean_string(price.text)
    address = address.text.strip().replace('|', '')
    url = url.get_attribute("href")

    # Create data frame row
    temp_DF = pd.DataFrame({'Address': [address], 'Price': [price], 'URL': [url]})
    results = pd.concat([results, temp_DF], ignore_index=True)

# Output results to CSV
results.to_csv('Summary.csv')
