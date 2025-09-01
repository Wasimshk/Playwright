from playwright.sync_api import expect
from page_object.home_page import Home
from page_object.modal import Modal

def test_modal(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    module = "Modal"
    homepage.open_module(module)
    modalpage = Modal(page, expect)
    modalpage.validate_module_page(module)
    modalpage.actions()
    homepage.redirect()

