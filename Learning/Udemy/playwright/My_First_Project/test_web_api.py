import json
from time import sleep

import pytest
from playwright.sync_api import Playwright, expect
from utils.api_base import Api_Utils
from pageObjects.login import LoginPage


# import json
with open("data/credentials.json", "r") as readerObj:
    test_data = json.load(readerObj)
    user_credentail_list = test_data["User_Creds"]


@pytest.mark.parametrize("userdata", user_credentail_list)
def test_e2e_web_api(playwright:Playwright, userdata):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # 1. Login (UI)
    loginPageObj = LoginPage(page)
    loginPageObj.navigate()
    loginPageObj.login(userdata)

    # 2. Create Order (API)
    apiUtiles = Api_Utils()
    orderID = apiUtiles.createOrder(playwright, userdata)

    if "wasim" in userdata['userEmail']:
        # 3. validate product(api)
        orderHistory = apiUtiles.getOrderHistory(playwright, userdata)
        assert orderID in orderHistory

    # # 3. validate product(UI)
        page.get_by_role("button", name="ORDERS").click()
        productRow = page.locator("tr").filter(has_text=orderID)
        productRow.get_by_role("button", name="View").click()
        expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    page.close()
    context.close()