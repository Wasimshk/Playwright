from playwright.sync_api import Page, expect
import pytest

@pytest.mark.ui
def test_ui_validations(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    samsungproduct = page.locator("app-card").filter(has_text="Samsung")
    samsungproduct.get_by_role("button").click()
    nokiaproduct = page.locator("app-card").filter(has_text="Nokia")
    nokiaproduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator("div.media-body")).to_have_count(2)
    samsung_in_cart = page.locator("div.media-body").filter(has_text="Samsung")
    expect(samsung_in_cart).to_contain_text("Samsung")
    nokia_in_cart = page.locator("div.media-body").filter(has_text="Nokia")
    expect(nokia_in_cart).to_contain_text("Nokia")
    page.get_by_role("button", name="Checkout").click()
    page.locator("#country").fill("India")
    page.locator("label[for='checkbox2']").check()
    # page.get_by_role("button").click()
    # page.get_by_role("button", name="Purchase").click()
    # expect(page.locator("div.alert-success")).to_contain_text("Success! Thank you! ")
