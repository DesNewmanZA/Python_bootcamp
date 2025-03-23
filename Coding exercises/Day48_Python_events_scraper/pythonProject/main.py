# Import needed modules
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org/events/")

# Get all events
raw_events = driver.find_elements(By.CLASS_NAME, "list-recent-events.menu")
events_list = []
for event in raw_events:
    events_list.append(event.text)

# Keep only upcoming events
events_list = events_list[1].split('\n')

# Process the events
events_dict = {}
for i in range(0, len(events_list), 3):
    print()
    events_dict[(i+1)//3] = {'name': events_list[i],
                             'time': events_list[i+1]}

print(events_dict)

# Close driver
driver.quit()