from time import sleep

from playwright.sync_api import expect


def test_scroll(formy_setup):
    page = formy_setup
    page.get_by_role("link", name="Page Scroll").click()
    expect(page.locator("h1")).to_have_text("Large page content")

    page.get_by_placeholder("Full name").scroll_into_view_if_needed()
    page.get_by_placeholder("Full name").fill("Wasim Shaikh")
    expect(page.get_by_placeholder("Full name")).to_have_value("Wasim Shaikh")
    page.get_by_placeholder("MM/DD/YYYY").fill("02/11/1996")
    expect(page.get_by_placeholder("MM/DD/YYYY")).not_to_be_empty()