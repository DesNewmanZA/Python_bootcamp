# Import needed modules
import pyautogui
import keyboard
import time
import numpy as np

# Start the game
time.sleep(2)
pyautogui.press('space')

# Loop indefinitely until an exit condition is met
while True:
    # Create a screenshot with each loop to decide what to do
    capture = pyautogui.screenshot()
    screen = capture.getpixel((214, 189))

    x1 = capture.getpixel((214, 189))
    x2 = capture.getpixel((214, 189))
    x3 = capture.getpixel((214, 189))
    x4 = capture.getpixel((214, 189))

    y1 = capture.getpixel((214, 189))
    y2 = capture.getpixel((214, 189))
    y3 = capture.getpixel((214, 189))
    y4 = capture.getpixel((214, 189))
    # capture.show()
    # time.sleep(0.5)
    # break

    pixels = np.array(capture)
    obstacle_pixels = pixels[:int(pixels.shape[0] * 0.6), :]

    # If there is an obstacle, jump
    if np.min(obstacle_pixels) < 100:
        pyautogui.press('space')
        time.sleep(0.01)

    # Exit condition - pressing q to quit
    if keyboard.is_pressed('q'):
        break
