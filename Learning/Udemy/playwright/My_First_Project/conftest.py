import pytest
from playwright.sync_api import Playwright

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chromium", help="Browser Name options: Chromium, firefox, edge, webkit, chrome"
    )

@pytest.fixture
def browser_instance(playwright:Playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)
    elif browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False, channel="chrome")
    elif browser_name == "edge":
        browser = playwright.chromium.launch(headless=False, channel="msedge")

    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()

