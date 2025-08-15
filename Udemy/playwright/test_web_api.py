import time
from time import sleep

from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # UI login
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("wasimahmad4210@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Automation@4210")
    page.get_by_role("button", name="Login").click()

    # create_order -> to get token and orderID
    api_utils = APIUtils()
    orderID = api_utils.createOrder(playwright)
    print(orderID)

    # order history page-> to validate order is present
    # # validating the order ID through API GET call
    orderHistory = api_utils.getOrderHistory(playwright)
    print(orderHistory)
    assert orderID in orderHistory
    # # validating the order ID through UI and clicking the view button and validate the page

    page.get_by_role("button", name="ORDERS").click()

    productRow = page.locator("tr").filter(has_text=orderID)
    productRow.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    context.close()

