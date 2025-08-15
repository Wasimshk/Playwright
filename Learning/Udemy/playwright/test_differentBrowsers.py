from playwright.sync_api import Page, Playwright

def test_chromiumbrowser(page:Page):
    # by default Playwright uses bundled chromium, which installed with playwright so we can skip creating a browser object through playwright fixture and directly use page fixture
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

def test_firefoxbrowser(playwright:Playwright):
    # to run tests on firefox, we not need to install the browser as chromium, firefox and WebKit get installed with the playwright
    firefoxBrowser = playwright.firefox
    browser = firefoxBrowser.launch(headless=False)
    # browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

def test_webkitbrowser(playwright:Playwright):
    webkitBrowser = playwright.webkit.launch(headless=False)
    page = webkitBrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

def test_chromebrowser(playwright:Playwright):
    chromeBrowser = playwright.chromium.launch(headless=False, channel="chrome")
    # There are two ways to run tests on chrome or edge, 1.use executable path argument 2. channel arguments
    # chromeBrowser = playwright.chromium.launch(headless=False, executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe")
    page = chromeBrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

def test_edgebrowser(playwright:Playwright):
    # There are two ways to run tests on chrome or edge, 1.use executable path argument 2. channel arguments
    # edgeBrowser = playwright.chromium.launch(headless=False, executable_path="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
    edgeBrowser = playwright.chromium.launch(headless=False, channel="msedge")
    page = edgeBrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()