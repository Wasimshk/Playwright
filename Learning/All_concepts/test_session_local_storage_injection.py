import pytest
from playwright.sync_api import Playwright, expect
from apibase import Api_Utils

@pytest.mark.session_local_storage
def test_session_storage(playwright:Playwright):
    apiutils_obj = Api_Utils()
    token = apiutils_obj.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # script to inject token into session local storage
    page.add_init_script(f"""localStorage.setItem('token', '{token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.locator("h1")).to_have_text("Your Orders")