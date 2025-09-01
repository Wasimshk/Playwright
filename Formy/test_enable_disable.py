from time import sleep

from playwright.sync_api import expect


def test_enable_disable(formy_setup):
    page = formy_setup
    page.get_by_role("link", name="Enabled and disabled elements").click()

    expect(page.locator("h1")).to_have_text("Enabled and Disabled elements")
    expect(page.get_by_placeholder("Disabled input here...")).to_be_disabled()
    expect(page.get_by_placeholder("Disabled input here...")).not_to_be_editable()
    expect(page.locator("#input")).to_be_enabled()
    expect(page.locator("#input")).to_be_editable()
    page.locator("#input").fill("Wasim Shaikh")
    expect(page.locator("#input")).to_have_value("Wasim Shaikh")
