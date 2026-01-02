# A simple automation to move pictures into folders by date - I do this manually when I've come back from a trip

# Import needed modules
import os
import shutil
from datetime import datetime

# Define source folder to sort
source_folder = os.path.normpath(input("Please input a path to sort: "))

# Create output folder with sorted photos
destination_folder = os.path.join(source_folder, "Sorted")
os.makedirs(destination_folder, exist_ok=True)

# Loop through all files in the source folder and sort into date stamped folders
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    # If file path is a file, then proceed. Else skip this iteration
    if os.path.isdir(file_path):
        continue

    # Find the creation date
    creation_time = os.path.getmtime(file_path)
    date_taken = datetime.fromtimestamp(creation_time).strftime("%Y_%m_%d")

    # Create a folder for this date - if it exists, this will just remain as is
    date_folder = os.path.join(destination_folder, date_taken)
    os.makedirs(date_folder, exist_ok=True)

    # Move the file to the folder
    shutil.move(file_path, os.path.join(date_folder, filename))
