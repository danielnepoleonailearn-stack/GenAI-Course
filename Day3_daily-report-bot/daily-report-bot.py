
# ============================================================
# Assignment: Fetch Weather Data and Save in Excel
# Description: Open AccuWeather, copy webpage content,
#              and save it in an Excel workbook.
# ============================================================

# 1. Import required libraries
import pyautogui
import time
from datetime import datetime


# 2. Initialize date and time variables
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
today_date = datetime.now().strftime("%Y-%m-%d")

# 3. Define constants and input data
weather_url = "https://www.accuweather.com/en/in/india-weather"
comment = "Good for outdoor activities"
filename = f"Weather_Report_{today_date}.xlsx"


# ============================================================
# 4. Open Firefox and fetch weather webpage content
# ============================================================

# Open Firefox
pyautogui.press("win")
pyautogui.write("firefox", interval=0.2)
pyautogui.press("enter")
time.sleep(4)

# Navigate to AccuWeather
pyautogui.write(weather_url, interval=0.02)
pyautogui.press("enter")
time.sleep(4)

# Copy the complete webpage content
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")
time.sleep(1)


# ============================================================
# 5. Open Microsoft Excel and create a new workbook
# ============================================================

# Open Excel
pyautogui.press("win")
pyautogui.write("excel", interval=0.2)
pyautogui.press("enter")
time.sleep(4)

# Create a new workbook
pyautogui.hotkey("ctrl", "n")
time.sleep(3)


# ============================================================
# 6. Enter headers and weather information
# ============================================================

# Enter column headers
pyautogui.write("Date & Time")
pyautogui.press("tab")
pyautogui.write("Fetched Data")
pyautogui.press("tab")
pyautogui.write("Comment")

# Move to the next row
pyautogui.press("enter")

# Enter current date and time
pyautogui.write(current_datetime)
pyautogui.press("tab")

# Paste webpage content into a single cell
pyautogui.press("f2")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# Enter comment
pyautogui.press("tab")
pyautogui.write(comment)

# ============================================================
# 7. Take screenshot and save it
# ============================================================

pyautogui.screenshot("weather_report.png")

# ============================================================
# 8. Save the Excel workbook
# ============================================================

pyautogui.hotkey("ctrl", "s")
time.sleep(2)

# Enter filename
pyautogui.write(filename, interval=0.1)
pyautogui.press("enter")
time.sleep(3)


# ============================================================
# 8. Completion message
# ============================================================

print(f"Weather report saved successfully: {filename}")
