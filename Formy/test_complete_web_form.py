from playwright.sync_api import expect
from page_object.home_page import Home
from page_object.webform import Webform

def test_complete_web_form(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    module = "Complete Web Form"
    homepage.open_module(module)
    webformpage = Webform(page, expect)
    webformpage.validate_module_page(module)
    webformpage.actions()
    expect(page.locator("h1")).to_contain_text("Thanks for submitting")
    homepage.redirect()



