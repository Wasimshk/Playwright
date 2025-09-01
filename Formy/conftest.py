from time import sleep

import pytest
from playwright.sync_api import Playwright, expect


def pytest_addoption(parser):
    parser.addoption(
        "--browserName", action="store", default="chromium", help="Browser Name options: chromium, firefox, edge, webkit, chrome"
    )

@pytest.fixture
def formy_setup(playwright:Playwright, request):
    browser_name = request.config.getoption("browserName")
    match browser_name:
        case "firefox":
            browser = playwright.firefox.launch(headless=False)
        case "webkit":
            browser = playwright.webkit.launch(headless=False)
        case "chrome":
            browser = playwright.chromium.launch(headless=False, channel="chrome")
        case "edge":
            browser = playwright.chromium.launch(headless=False, channel="msedge")
        case _:
            browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://formy-project.herokuapp.com/")
    expect(page.locator("h1")).to_have_text("Welcome to Formy")
    yield page
    page.locator("#logo").click()
    # validate home page
    expect(page.locator("h1")).to_have_text("Welcome to Formy")
    sleep(0.5)
    page.close()
    context.close()
    browser.close()



