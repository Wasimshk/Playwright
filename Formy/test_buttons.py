from time import sleep
from playwright.sync_api import Playwright, expect, Page
from page_object.home_page import Home
from page_object.buttons import Buttons

def test_buttons(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    module = "Buttons"
    homepage.open_module(module)
    buttonspage = Buttons(page, expect)
    buttonspage.validate_module_page()
    buttonspage.actions()
    homepage.redirect()






