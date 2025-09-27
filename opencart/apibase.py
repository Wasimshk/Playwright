from playwright.sync_api import Playwright

base_url = "https://www.opencart.com/index.php"
params = {
    "route": "account/account",
    "member_token": "9de675ef50e94317283afe8e876f3fc9"   # replace with dynamic token
}

class APICalls:
    # def __init__(self):
    #     pass

    def login(self, playwright:Playwright):
        context = playwright.request.new_context("https://www.opencart.com")
        response = context.post(url="/index.php")
        assert response.ok
        if response.status == 200:
            text = response.text()
            print(text)
        #     assert "OpenCart - Your Account" in text
        else:
            print(f"Failed to retrieve the page. Status code: {response.status}")