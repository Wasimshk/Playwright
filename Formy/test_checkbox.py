from time import sleep
from playwright.sync_api import expect
from page_object.home_page import Home
from page_object.checkboxes import Checkboxes


def test_checkbox(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    module = "Checkbox"
    homepage.open_module(module)
    checkboxespage = Checkboxes(page, expect)
    checkboxespage.validate_module_page("Checkboxes")
    checkboxespage.actions()
    homepage.redirect()
