import json
from time import sleep

import pytest
from playwright.sync_api import Playwright, expect
from utils.api_base import Api_Utils

# import json
with open("data/credentials.json", "r") as readerObj:
    test_data = json.load(readerObj)
    user_credentail_list = test_data["User_Creds"]


@pytest.mark.parametrize("userdata", user_credentail_list)
def test_e2e_web_api(playwright:Playwright, userdata):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    Email = userdata['userEmail']
    Password = userdata['userPassword']

    # 1. Login (UI)
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill(Email)
    page.get_by_placeholder("enter your passsword").fill(Password)
    page.get_by_role("button", name="Login").click()

    # 2. Create Order (API)
    apiUtiles = Api_Utils()
    orderID = apiUtiles.createOrder(playwright, userdata)

    if "wasim" in Email:
        # 3. validate product(api)
        orderHistory = apiUtiles.getOrderHistory(playwright, userdata)
        assert orderID in orderHistory

    # # 3. validate product(UI)
        page.get_by_role("button", name="ORDERS").click()
        productRow = page.locator("tr").filter(has_text=orderID)
        productRow.get_by_role("button", name="View").click()
        expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
        sleep(2)
    page.close()
    context.close()