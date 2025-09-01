from time import sleep

from playwright.sync_api import expect


def test_dropdown(formy_setup):
    page = formy_setup
    page.get_by_role("link", name="Dropdown").click()

    expect(page.locator("h1")).to_have_text("Dropdown")
    page.locator("#dropdownMenuButton").click()
    page.locator('[class="dropdown-menu show"] > a').filter(has_text="Checkbox").click()
