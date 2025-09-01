from playwright.sync_api import expect
from page_object.home_page import Home

def test_radio_button(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    page.get_by_role("link", name="Radio Button").click()
    expect(page.locator("h1")).to_have_text("Radio buttons")

    # page.get_by_role("radio", name="Radio button 1").click()
    expect(page.get_by_role("radio", name="Radio button 1")).to_be_checked()

    page.locator('[value="option2"]').click()
    expect(page.locator('[value="option2"]')).to_be_checked()
    homepage.redirect()

    # using xpath and sibling approach
    # page.locator(xpath='//label[@class="form-check-label"]/preceding-sibling::input[@value="option3"]').click()
    # expect(page.locator(xpath='//input[@value="option3"]')).to_be_checked()

