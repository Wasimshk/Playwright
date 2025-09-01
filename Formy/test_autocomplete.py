from time import sleep
from playwright.sync_api import Playwright, expect
from page_object.home_page import Home
from page_object.autocomplete import Autocomplete

def test_autocomplete(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    module = "Autocomplete"
    homepage.open_module(module)
    autocompletepage = Autocomplete(page, expect)
    autocompletepage.validate_module_page(module)
    autocompletepage.actions()
    homepage.redirect()










