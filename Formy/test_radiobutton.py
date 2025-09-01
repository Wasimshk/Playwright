from playwright.sync_api import expect
from page_object.home_page import Home
from page_object.radio import Radio

def test_radio_button(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    module = "Radio Button"
    homepage.open_module(module)
    radiopage = Radio(page, expect)
    radiopage.validate_module_page("Radio buttons")
    radiopage.actions()
    homepage.redirect()

