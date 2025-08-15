from http.client import responses

from playwright.sync_api import Playwright

baseUrl = "https://rahulshettyacademy.com"

loginPayload = {"userEmail": "wasimahmad4210@gmail.com", "userPassword": "Automation@4210"}

ordersPayload = {
    "orders": [
        {
            "country": "India",
            "productOrderedId": "67a8df56c0d3e6622a297ccd"
        }
    ]
}
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2ODdjYTZlYjZlYjM3Nzc1MzBhYTg0OGYiLCJ1c2VyRW1haWwiOiJ3YXNpbWFobWFkNDIxMEBnbWFpbC5jb20iLCJ1c2VyTW9iaWxlIjo4NjY4NTU2MTYwLCJ1c2VyUm9sZSI6ImN1c3RvbWVyIiwiaWF0IjoxNzUzMDA0NzA4LCJleHAiOjE3ODQ1NjIzMDh9.MI0sAEDFmme1_vWh5MzA41kTNXURGJ1e3OWm7xXZ1Mo"
# ordersHeaders = {"Authorization":token, "content-type":"application/json"}

class APIUtils:

    def getToken(self, playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url=baseUrl)
        response = api_request_context.post("/api/ecom/auth/login", data=loginPayload)
        assert response.ok
        # print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def createOrder(self, playwright:Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url=baseUrl)
        response = api_request_context.post("/api/ecom/order/create-order", data=ordersPayload, headers={"Authorization":token, "content-type":"application/json"})
        # print(response.json())
        responseBody =response.json()
        orderID = responseBody["orders"][0]
        return orderID

    def getOrderHistory(self, playwright:Playwright):
        token = self.getToken(playwright)
        api_request_context= playwright.request.new_context(base_url=baseUrl)
        response = api_request_context.get("/api/ecom/order/get-orders-for-customer/687ca6eb6eb3777530aa848f", headers={"Authorization":token, "content-type":"application/json"})
        responseBody = response.json()
        orderIDs = [item["_id"] for item in responseBody["data"]]
        # the above line is same as the below one
        # orderIDs = []
        # for item in responseBody["data"]:
        #     orderIDs.append(item["_id"])
        return orderIDs