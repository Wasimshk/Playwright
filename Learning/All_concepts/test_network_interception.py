import pytest
from playwright.sync_api import Page, expect


# --------Response interception--------
fakeEmptyOrderResponsePayload = {"data":[],"message":"No Orders"}
def intercept_response(route):
    route.fulfill(json=fakeEmptyOrderResponsePayload)

@pytest.mark.interception
def test_network_interception(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    # page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", lambda route: route.fulfill(json=fakeEmptyOrderResponsePayload))
    page.get_by_placeholder("email@example.com").fill("wasimahmad4210@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Automation@4210")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    expect(page.locator(".mt-4")).to_contain_text("No Orders ")


# --------request interception--------
def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=68a35f996f585eb60d8260fa")

@pytest.mark.interception
def test_network_Interception2(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("wasimahmad4210@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Automation@4210")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)
    # expect(page.locator(".blink_me")).to_have_text("You are not authorize to view this order")
