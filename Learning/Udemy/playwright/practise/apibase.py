from playwright.sync_api import Playwright

loginPayload = {"userEmail":"wasimahmad4210@gmail.com","userPassword":"Automation@4210"}
createOrderPayload = {"orders":[{"country":"Australia","productOrderedId":"67a8df56c0d3e6622a297ccd"}]}

class Api_Utils:
    def getToken(self, playwright:Playwright):
        apicontext = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = apicontext.post(url="/api/ecom/auth/login", data=loginPayload)
        assert response.ok
        responseBody = response.json()
        print(responseBody["token"])
        return responseBody["token"]

    def createOrder(self, playwright:Playwright):
        token = self.getToken(playwright)
        apiContext = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = apiContext.post(url="/api/ecom/order/create-order", data= createOrderPayload, headers={"Authorization":token, "content-type": "application/json"})
        responseBody = response.json()
        print(responseBody["orders"][0])
        return responseBody["orders"][0]

    def getOrderHistory(self, playwright:Playwright):
        token = self.getToken(playwright)
        apiContext = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = apiContext.get("/api/ecom/order/get-orders-for-customer/687ca6eb6eb3777530aa848f", headers={"Authorization":token,"content-type": "application/json"})
        responseBody = response.json()
        orderIDs = [item_dict["_id"] for item_dict in responseBody["data"]]
        print(orderIDs)
        return orderIDs
