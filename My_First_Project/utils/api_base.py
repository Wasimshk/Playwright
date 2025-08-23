from playwright.sync_api import Playwright

createOrderPayload = {"orders":[{"country":"Australia","productOrderedId":"68a864dfb01c5d7abb27e636"}]}

class Api_Utils:
    def getToken(self, playwright:Playwright, userdata):

        Email = userdata['userEmail']
        Password = userdata['userPassword']
        loginPayload = {"userEmail": Email, "userPassword": Password}

        apicontext = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = apicontext.post(url="/api/ecom/auth/login", data=loginPayload)
        assert response.ok
        responseBody = response.json()
        print(responseBody["token"])
        return responseBody["token"]

    def createOrder(self, playwright:Playwright, userdata):
        token = self.getToken(playwright, userdata)
        apiContext = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = apiContext.post(url="/api/ecom/order/create-order", data= createOrderPayload, headers={"Authorization":token, "content-type": "application/json"})
        responseBody = response.json()
        print(responseBody["orders"][0])
        return responseBody["orders"][0]

    def getOrderHistory(self, playwright:Playwright, userdata):
        token = self.getToken(playwright, userdata)
        apiContext = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = apiContext.get("/api/ecom/order/get-orders-for-customer/687ca6eb6eb3777530aa848f", headers={"Authorization":token,"content-type": "application/json"})
        responseBody = response.json()
        orderIDs = [item_dict["_id"] for item_dict in responseBody["data"]]
        print(orderIDs)
        return orderIDs
