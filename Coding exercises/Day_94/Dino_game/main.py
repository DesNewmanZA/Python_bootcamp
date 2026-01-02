# Import needed modules
import pyautogui
from pyautogui import ImageNotFoundException
import keyboard
import time
import numpy as np

# The user must have a tab open with chrome://dino/ - from here, when pressing run, they swap to the tab to begin

# Start the game
time.sleep(2)
pyautogui.press('space')

# Find dinosaur location
dino_location = pyautogui.locateOnScreen("dino.png", confidence=0.7, grayscale=True)

# Loop indefinitely until an exit condition is met
while True:
    # Check if game is still going
    try:
        game_over = pyautogui.locateOnScreen("game_over.PNG", confidence=0.7, grayscale=True)
    except ImageNotFoundException:
        game_over = None

    if game_over is not None:
        break

    # Define area where to look for obstacles
    x = int(dino_location.left + dino_location.width + 20)
    y = int(dino_location.top)
    width = 100  # Number of pixels ahead to look
    height = int(dino_location.height * 0.8)  # Ignoring the group

    # Create a screenshot with each loop to decide what to do
    capture = pyautogui.screenshot(region=(x, y, width, height)).convert('L')
    pixels = np.array(capture)
    obstacle_pixels = pixels[:int(pixels.shape[0] * 0.6), :]

    # If there is an obstacle, jump
    if np.min(obstacle_pixels) < 100:
        pyautogui.press('space')
        time.sleep(0.01)

    # Exit condition - pressing q to quit
    if keyboard.is_pressed('q'):
        break
