# Import needed modules
import pandas as pd

# Read in the data and get a feel for the columns available
my_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# Make a summary of the squirrels by colour
colour_summary = my_data.groupby(['Primary Fur Color'])[['Primary Fur Color']].count().rename(columns={'Primary Fur Color' : 'Count'}).rename_axis(index=None)
colour_summary.to_csv('squirrel_count.csv')