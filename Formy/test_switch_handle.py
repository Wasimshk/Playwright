from playwright.sync_api import expect
from page_object.home_page import Home
from page_object.windowhandle import Windowhandle

def test_child_window(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    module = "Switch Window"
    homepage.open_module(module)
    windowpage = Windowhandle(page, expect)
    windowpage.validate_module_page(module)
    windowpage.child_window_action()
    homepage.redirect()


def test_dialog_box(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    module = "Switch Window"
    homepage.open_module(module)
    windowpage = Windowhandle(page, expect)
    windowpage.validate_module_page(module)
    windowpage.dialog_action()
    homepage.redirect()