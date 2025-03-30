# Import needed modules
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://appbrewery.github.io/instant_pot/")

# Get the price
price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole").text
price_frac = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
print(f"The price is ${price_whole}.{price_frac}")

# Close driver  
driver.quit()