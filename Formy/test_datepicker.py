import pytest
from playwright.sync_api import expect
from page_object.home_page import Home
from page_object.datepicker import Datepicker

@pytest.mark.parametrize("birthdate", ["02/11/1996", "02/20/1997", "01/12/2024" ])
def test_datepicker(formy_setup, birthdate):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    module = "Datepicker"
    homepage.open_module(module)
    datepickerpage = Datepicker(page, expect)
    datepickerpage.validate_module_page(module)
    datepickerpage.actions(birthdate)
    homepage.redirect()


