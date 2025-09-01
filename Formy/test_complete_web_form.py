from playwright.sync_api import expect
from page_object.home_page import Home

def test_complete_web_form(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    page.get_by_role("link", name="Complete Web Form").click()
    expect(page.locator("h1")).to_have_text("Complete Web Form")

    page.get_by_label("First name").fill("Wasim")
    page.get_by_label("Last name").fill("Shaikh")
    page.get_by_label("Job title").fill("SDET")
    page.locator("#radio-button-3").check()
    expect(page.locator("#radio-button-3")).to_be_checked()
    page.locator("#checkbox-1").check()
    expect(page.locator("#checkbox-1")).to_be_checked()
    page.locator("#select-menu").select_option("3")
    page.get_by_placeholder("mm/dd/yyyy").fill("02/11/1996")
    expect(page.get_by_placeholder("mm/dd/yyyy")).not_to_be_empty()
    page.get_by_role("button", name="Submit").click()

    expect(page.locator("h1")).to_contain_text("Thanks for submitting")
    homepage.redirect()



