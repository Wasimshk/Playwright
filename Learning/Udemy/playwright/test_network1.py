import time

from playwright.sync_api import Page

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}
# api call from browser >> api call contact server return back response to browser >> browser use reponse to generate the html
def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )

def test_network1(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    # route is the listener, it accept 2 argument, 1. event, 2. work should be done once it encounters the event
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("wasimahmad4210@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Automation@4210")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)
    time.sleep(2)