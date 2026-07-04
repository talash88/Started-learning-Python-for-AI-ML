# This Python program uses the PyAutoGUI library to automate mouse and keyboard actions. First, the program waits for 5 seconds so the user can switch to any application like Notepad, browser, or chat window.
# After that, the program moves the mouse cursor to a specific position on the screen and performs a click to activate the input area. Once the input box is active, it automatically types a given message using the keyboard automation feature.
# Finally, the program presses the Enter key to send the message or move to a new line.



import pyautogui
import time

# Wait for 5 seconds to switch to another window
time.sleep(5)

# Move mouse to a specific position on the screen
pyautogui.moveTo(500, 300)

# Click at that position to focus the input box
pyautogui.click()

# Type the given text automatically
pyautogui.write("Hello! I am controlling mouse and typing using Python ", interval=0.1)

# Press Enter key to send message or move to next line
pyautogui.press("enter")

