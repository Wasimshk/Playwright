from playwright.sync_api import expect
from page_object.home_page import Home
from page_object.scroll import Scroll

def test_scroll(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    module = "Page Scroll"
    homepage.open_module(module)
    scrollpage = Scroll(page, expect)
    scrollpage.validate_module_page("Large page content")
    scrollpage.actions()
    homepage.redirect()