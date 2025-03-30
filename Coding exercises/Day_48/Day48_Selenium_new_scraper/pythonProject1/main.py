# Import needed modules
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Get the results
num_articles = driver.find_elements(By.CSS_SELECTOR, "#articlecount a")
res_list = []
for article in num_articles:
    res_list.append(article.text)

# Print out the result
print(f"Number of articles: {res_list[1]}")

# Close driver
driver.quit()