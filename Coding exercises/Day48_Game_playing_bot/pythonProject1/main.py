# Unoptimised algorithm - using algorithm proposed by lesson

# Import needed modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Cookie location
cookie = driver.find_element(By.ID, "cookie")

# Upgrades location - stays static so single search
upgrades = driver.find_elements(By.CSS_SELECTOR, "#store div")
upgrades_ids = [item.get_attribute("id") for item in upgrades]

# Loop for 5 minutes
five_min_timer = time.time() + 60*5
five_seconds = time.time() + 5

while time.time() < five_min_timer:
    # Continuously click cookie while timer active
    cookie.click()

    # If 5 seconds have passed
    if time.time() > five_seconds:
        # Get current money value to see what upgrades can be bought
        money_element = driver.find_element(By.ID, "money")
        money = int(money_element.text.replace(',', ""))

        # Check upgrades and see what is within buying power
        prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        upgrade_item = ''
        # There are 8 upgrade items
        for i in range(8):
            value = int(prices[i].text.split('-')[1].strip().replace(',', ''))
            if value <= money:
                upgrade_item = upgrades_ids[i]
        # Buy the most expensive one available
        if upgrade_item != '':
            upgrade_button = driver.find_element(By.ID, upgrade_item)
            upgrade_button.click()

        five_seconds = time.time() + 5

# Find final cookies per second
score = driver.find_element(By.ID, "cps").text
print(score)
