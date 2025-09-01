import random
from time import sleep

import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize("birthdate", ["02/11/1996", "02/20/1997", "01/12/2024" ])
def test_datepicker(formy_setup, birthdate):
    page = formy_setup
    page.get_by_role("link", name="Datepicker").click()

    expect(page.locator("h1")).to_have_text("Datepicker")
    page.get_by_placeholder("mm/dd/yyyy").fill(birthdate)
    expect(page.get_by_placeholder("mm/dd/yyyy")).not_to_be_empty()
    expect(page.get_by_placeholder("mm/dd/yyyy")).to_have_value(birthdate)


