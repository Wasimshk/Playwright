from playwright.sync_api import Playwright

from Formy.webscraping.sample import response


def test_login(playwright:Playwright):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    #
    #
    #
    # page.goto("https://www.opencart.com/index.php?route=account/login")
    # # page.locator(".btn-link").click()
    # page.get_by_text("Log in to your OpenCart account").wait_for(state="visible")
    # page.get_by_label("Email").fill("wasim.shaikh.allpro@gmail.com")
    # page.get_by_label("Password").fill("Wasim@4210")
    # page.get_by_role("button", name="Login").click()


















    # base_url = "https://www.opencart.com/index.php"
    # payload = {
    #     "email": "wasim.shaikh.allpro@gmail.com",
    #     "password": "Wasim@4210"
    # }
    #
    # params = {
    #     "route": "account/account",
    #     # "member_token": "f6cdd29f312980a0a56b57d0138cf629"
    # }
    # context = playwright.request.new_context(base_url="https://www.opencart.com/index.php")
    # postresponse = context.post(url="?route=account/login")
    # if postresponse.status == 200:
    #     text = postresponse.text()
    #     print(text)
    # else:
    #     print(f"Failed to retrieve the page. Status code: {postresponse.status}")



    # response = context.get(url="/index.php?route=account/account&member_token=f6cdd29f312980a0a56b57d0138cf629")
    # assert response.ok
    # if response.status == 200:
    #     text = response.text()
    #     print(text)
    # #     assert "OpenCart - Your Account" in text
    # else:
    #     print(f"Failed to retrieve the page. Status code: {response.status}")

