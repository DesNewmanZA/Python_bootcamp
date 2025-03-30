# Import needed modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# Get the results
fname_element = driver.find_element(By.NAME, "fName")
fname_element.send_keys("Joe", Keys.ENTER)

lname_element = driver.find_element(By.NAME, "lName")
lname_element.send_keys("Soap", Keys.ENTER)

mail_element = driver.find_element(By.NAME, "email")
mail_element.send_keys("joesoap@testing.co.za", Keys.ENTER)

button_element = driver.find_element(By.CSS_SELECTOR, 'form button')
button_element.click()

# Close driver
# driver.quit()