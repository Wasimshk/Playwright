import json
from time import sleep

import pytest
from playwright.sync_api import Playwright, expect
from utils.api_base import Api_Utils
from pageObjects.login import LoginPage
from pageObjects.dashboard import DashBoardPage
from pageObjects.orderhistory import OrderHistoryPage
from pageObjects.ordersummary import OrderSummaryPage

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
    # dashboardPageObj = loginPageObj.login(userdata) # use this when we return dashboard page object from login page class

    # 2. Create Order (API)
    apiUtiles = Api_Utils()
    orderID = apiUtiles.createOrder(playwright, userdata)

    if "wasim" in userdata['userEmail']:
        # 3.a validate product(api)
        orderHistory = apiUtiles.getOrderHistory(playwright, userdata)
        assert orderID in orderHistory

        # 3.b validate product(UI)
        # click orders button to navidate to order history page
        dashboardPageObj = DashBoardPage(page)
        dashboardPageObj.select_orders_nav_link()

        # validate if order is created and shows in order history
        orderHistoryPageObj = OrderHistoryPage(page)
        orderHistoryPageObj.validate_order_id(orderID)

        # view order summary
        orderSummaryPageObj = OrderSummaryPage(page)
        orderSummaryPageObj.view_order_Summary()

    page.close()
    context.close()