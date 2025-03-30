# Import needed modules
import csv
import pandas as pd

# Open the data file
with open('weather_data.csv') as my_file:
    contents = csv.reader(my_file)
    # Create list to store temperatures
    temperatures = []
    # Only save the data, not the column name
    count = 0
    for row in contents:
        if count != 0:
            temperatures.append(int(row[1]))
        count += 1

# Alternative with pandas
my_data = pd.read_csv('weather_data.csv')

# Calculate average temperature
avg_temp = my_data['temp'].mean()
print(f"The average temperature was {avg_temp}")

# Calculate maximum temperature
max_temp = my_data['temp'].max()
print(f"The maximum temperature was {max_temp}")

# Extract the row with the maximum temperature
print(my_data[my_data['temp'] == max_temp])

# Get Monday's temperature and convert to Farenheit
monday_temp = my_data[my_data.day == 'Monday']['temp'][0]
monday_temp_f = (9 / 5) * monday_temp + 32
print(f"The temperature on Monday is {monday_temp}C or {monday_temp_f}F.")
