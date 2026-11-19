import pyautogui

pyautogui.typewrite("Hello, this is an automated message!")  # Type a message
pyautogui.press("a")  # Press the Enter key
pyautogui.hotkey("shift", "s", "a")  # Press Ctrl + S to save
pyautogui.keyDown("shift")  # Hold down the Shift key
pyautogui.press("z")  # Press the 'A' key while Shift is held down
pyautogui.keyUp("shift")  # Release the Shift key

pyautogui.screenshot("screenshot.png") # Take a screenshot and save it as "screenshot.png"