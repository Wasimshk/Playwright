import time
from time import sleep

import pytest
from playwright.sync_api import Page, expect, Playwright

from apibase import Api_Utils


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

# API + UI (E2E testing)
"""

1. login
login manually or though UI: add username and password and click login button
    from inspect>>network>>header section - we can get call method(GET\POST), request URL, status code
    from inspect>>network>>payload section - we can get the json body 
    from inspect>>network>>Response section - we can get authorization token, and complete response.

login through api call:
    in postman: 
    select method (GET\POST)
    add request URL
    add json
    
2. create order
manually or though UI: create order by adding item to cart and add the required details like country. 
    from inspect>>network>>header section - we can get call method(GET\POST), request URL, status code and Authorization token
    from inspect>>network>>payload section - we can get the json body 
    from inspect>>network>>Response section - we can get the complete response(e.g order id), in this case we will see the token at header section not in the response.
"""

def test_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

# 1. Login (UI)
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("wasimahmad4210@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Automation@4210")
    page.get_by_role("button", name="Login").click()

# 2. Create Order (API)
    apiUtiles = Api_Utils()
    orderID = apiUtiles.createOrder(playwright)

# 3. validate product(api)
    orderHistory = apiUtiles.getOrderHistory(playwright)
    assert orderID in orderHistory

# 3. validate product(UI)
    page.get_by_role("button", name="ORDERS").click()
    productRow = page.locator("tr").filter(has_text=orderID)
    productRow.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    sleep(2)
    page.close()
    context.close()


# network interception

# response interception
# validation >> what the html shows when there is zero orders in order history page?, to achieve this we will need to delete all the orders from order history which is not best practice, instead we will intercept the response and change the payload to achieve this scenario.

fakeEmptyOrderResponsePayload = {"data":[],"message":"No Orders"}
def intercept_response(route):
    route.fulfill(
        json=fakeEmptyOrderResponsePayload
    )

def test_network_interception(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    # event listener, this route method will use to intercept the network response, this listener will execute the event as soon as the below code hits the request url provided in the first argument, in this case the api request url - https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/* hits once the ORDERS button is clicked.
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("wasimahmad4210@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Automation@4210")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    # sleep(5)
    # print(page.locator(".mt-4").text_content())
    expect(page.locator(".mt-4")).to_contain_text("No Orders ")

# request call interception
# validation >> test the scenario when someone is trying to access your orders from your order history what will show, expectation is to see the unauthorization message. To achieve this we will intercept the request call. it more like a security test.

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=68a35f996f585eb60d8260fa")

def test_network_Interception2(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("wasimahmad4210@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Automation@4210")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    # sleep(5)
    print(message)
    # expect(page.locator(".blink_me")).to_have_text("You are not authorize to view this order")

def test_session_storage(playwright:Playwright):
    apiutils_obj = Api_Utils()
    token = apiutils_obj.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # script to inject token into session local storage
    page.add_init_script(f"""localStorage.setItem('token', '{token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.locator("h1")).to_have_text("Your Orders")

# parameterized tests (data driven tests)
@pytest.mark.parametrize("input", [2, 4, 8, 10, 5])
def test_even_numbers(input):
    assert input%2 == 0

@pytest.mark.parametrize("input1, input2, expected_output", [(1, 2, 3), (3, 9, 12), (0,0,0), (100, 0, 101)])
def test_addition(input1, input2, expected_output):
    assert input1 + input2 == expected_output











