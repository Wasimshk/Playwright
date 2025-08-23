from time import sleep

import pytest
from playwright.sync_api import Playwright, expect
from apibase import Api_Utils

@pytest.mark.e2e
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