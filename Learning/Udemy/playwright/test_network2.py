import time

from playwright.sync_api import Page

# api call from browser >> api call contact server return back response to browser >> browser use reponse to generate the html
def intercept_api_call(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=687e7c4e6eb3777530adffff")

def test_network1(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    # route is the listener, it accept 2 argument, 1. event, 2. work should be done once it encounters the event
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_api_call)
    page.get_by_placeholder("email@example.com").fill("wasimahmad4210@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Automation@4210")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)
    time.sleep(5)
