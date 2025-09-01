from playwright.sync_api import expect
from page_object.home_page import Home
from page_object.enabledisable import Enabledisable

def test_enable_disable(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    module = "Enabled and disabled elements"
    homepage.open_module(module)
    enabledisablepage = Enabledisable(page, expect)
    enabledisablepage.validate_module_page("Enabled and Disabled elements")
    enabledisablepage.actions()
    homepage.redirect()
