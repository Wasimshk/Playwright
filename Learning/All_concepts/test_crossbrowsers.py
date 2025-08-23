from playwright.sync_api import Playwright
import pytest

@pytest.mark.crosebrowser
def test_login_firefox(playwright:Playwright):
    firefoxbrowser = playwright.firefox.launch(headless=False)
    context = firefoxbrowser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()

@pytest.mark.crosebrowser
def test_login_webkit(playwright:Playwright):
    webkitbrowser = playwright.webkit.launch(headless=False)
    context = webkitbrowser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()

@pytest.mark.crosebrowser
def test_login_chrome(playwright:Playwright):
    chromebrowser = playwright.chromium.launch(headless=False, channel="chrome")
    # There are two ways to run tests on chrome or edge, 1.use executable path argument 2. channel arguments
    # chromeBrowser = playwright.chromium.launch(headless=False, executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe")
    # context = chromebrowser.new_context()
    page = chromebrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()

@pytest.mark.crosebrowser
def test_login_edge(playwright:Playwright):
    edgebrowser = playwright.chromium.launch(headless=False, channel="msedge")
    # There are two ways to run tests on chrome or edge, 1.use executable path argument 2. channel arguments
    # edgeBrowser = playwright.chromium.launch(headless=False, executable_path="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
    # context = edgebrowser.new_context()
    page = edgebrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
