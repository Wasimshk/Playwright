from time import sleep
from playwright.sync_api import Playwright, expect
from page_object.home_page import Home

def test_autocomplete(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    page.get_by_role("link", name="Autocomplete").click()
    expect(page.locator("h1")).to_have_text("Autocomplete")
    page.get_by_placeholder("Enter address").fill("lane 4")
    page.locator("#street_number").fill("block 4")
    page.get_by_placeholder("Street address 2").fill("area 4")
    page.get_by_placeholder("City").fill("Pune")
    page.get_by_placeholder("State").fill("Maharashtra")
    page.get_by_placeholder("Zip code").fill("411001")
    page.get_by_placeholder("Country").fill("India")
    homepage.redirect()










