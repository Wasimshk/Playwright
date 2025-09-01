
# To simulate typing a sequence of characters, use page.keyboard.type():
from playwright.sync_api import sync_playwright

def test_type_text():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.example.com")
        page.fill("input#search", "Playwright keyboard actions")
        page.keyboard.type(" and press Enter")
        browser.close()

#2. Pressing Individual Keys:
# To simulate pressing a specific key, use page.keyboard.press():

from playwright.sync_api import sync_playwright

def test_press_key():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.example.com")
        page.keyboard.press("Enter")  # Presses the Enter key
        browser.close()

# 3. Holding Down and Releasing Keys:
# For more granular control, use page.keyboard.down() to hold a key down and page.keyboard.up() to release it:

from playwright.sync_api import sync_playwright

def test_hold_and_release_key():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.example.com")
        page.keyboard.down("Shift")  # Holds down the Shift key
        page.keyboard.press("KeyA")  # Types 'A' while Shift is held (results in 'A')
        page.keyboard.up("Shift")    # Releases the Shift key
        browser.close()

# 4. Sending Key Combinations:
# To send key combinations (e.g., Ctrl+A), use page.keyboard.press() with a string representing the combination:
from playwright.sync_api import sync_playwright

def test_key_combination():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.example.com")
        page.keyboard.press("Control+a")  # Selects all text on the page
        browser.close()