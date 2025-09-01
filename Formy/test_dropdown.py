from playwright.sync_api import expect
from page_object.home_page import Home
from page_object.dropdown import Dropdown

def test_dropdown(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    module = "Dropdown"
    homepage.open_module(module)
    dropdownpage = Dropdown(page, expect)
    dropdownpage.validate_module_page(module)
    dropdownpage.actions()
    homepage.redirect()
