import time
from time import sleep

from playwright.sync_api import Page, expect, Playwright
# login tests
def test_login(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()

def test_login_invalid_creds(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("wrongusername")
    page.get_by_label("Password:").fill("wrongpasswork")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.locator(".alert-danger.alert")).to_have_text("Incorrect username/password.")

# login test with different browsers, chromium, firefox and Webkit(safari like) are inbuilt, for chrome and edge we will need channel or driver exe path
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


# UI validation - workflow from login to add items to cart and validate
def test_ui_validations(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    samsungproduct = page.locator("app-card").filter(has_text="Samsung")
    samsungproduct.get_by_role("button").click()
    nokiaproduct = page.locator("app-card").filter(has_text="Nokia")
    nokiaproduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator("div.media-body")).to_have_count(2)
    samsung_in_cart = page.locator("div.media-body").filter(has_text="Samsung")
    expect(samsung_in_cart).to_contain_text("Samsung")
    nokia_in_cart = page.locator("div.media-body").filter(has_text="Nokia")
    expect(nokia_in_cart).to_contain_text("Nokia")
    page.get_by_role("button", name="Checkout").click()
    page.locator("#country").fill("India")
    page.locator("label[for='checkbox2']").check()
    page.get_by_role("button", name="Purchase").click()
    expect(page.locator("div.alert-success")).to_contain_text("Success! Thank you! ")

# visible assertions
def test_visiblity(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    expect(page.get_by_placeholder("Hide/Show Example")).not_to_be_hidden()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).not_to_be_visible()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

# Handle Child window
def test_child_window(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as child_window:
        page.locator(".blinkingText").click()
        child_page = child_window.value
        # direct assertion
        expect(child_page.locator("p.red")).to_contain_text("mentor@rahulshettyacademy.com")

        # extract email and assert
        text = child_page.locator("p.red").text_content()

        # one way
        words = text.split("at ")
        word_list = words[1].split()
        email = word_list[0]
        print("Email extracted through split method: ", email)
        assert email == "mentor@rahulshettyacademy.com"

        # other way
        email = None
        words = text.split()
        for word in words:
            if "@" in word:
                email = word

        print("Email extracted through loop: ", email)
        assert email == "mentor@rahulshettyacademy.com"

# alert box
def test_alertbox(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog_event_argument: dialog_event_argument.accept())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(2)

# mouse hover
def test_mouse_hover(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.get_by_role("button", name="Mouse Hover").hover()
    page.get_by_role("link", name="Top").click()

# frame\iframe
def test_frame(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    frame_page = page.frame_locator("#courses-iframe")
    frame_page.get_by_role("link", name="All Access Plan").click()
    expect(frame_page.locator("body")).to_contain_text("Happy Subscibers!")

# web table
"""
Check the price of rice is equal to 37
identify the price column
identify rice row
extract the price of the rice
"""

def test_webtables(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    columnheader = page.locator("th[role='columnheader']")
    colValue = None
    for i in range(columnheader.count()):
        if columnheader.nth(i).filter(has_text="Price").count()>0:
            colValue = i
            print(f"Price Column Value is: {colValue}")
            break

    riceRow = page.locator("tr").filter(has_text="Rice")
    print("rice row: ", riceRow)
    expect(riceRow.locator("td").nth(colValue)).to_have_text("37")






