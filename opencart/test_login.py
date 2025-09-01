from playwright.sync_api import Playwright


def test_login(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.opencart.com")
    page.get_by_role()

