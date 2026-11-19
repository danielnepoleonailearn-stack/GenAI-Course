from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.cricbuzz.com/")
    matchScore = page.get_by_title("Sri Lanka vs Pakistan, 2nd Test ").all_inner_texts()
    print(f"Match Score Details: {matchScore}")
    page.screenshot(path="cricbuzz.png")
    browser.close()