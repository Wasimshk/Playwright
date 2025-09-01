from time import sleep

from playwright.sync_api import expect


def test_modal(formy_setup):
    page = formy_setup
    page.get_by_role("link", name="Modal").click()
    expect(page.locator("h1")).to_have_text("Modal")

    page.locator("#modal-button").click()
    expect(page.locator(".modal-title")).to_be_visible()
    # page.locator("button:has-text('Close')").click()
    page.locator("button").filter(has_text="Close").click()
    expect(page.locator(".modal-title")).not_to_be_visible()

