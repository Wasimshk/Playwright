from time import sleep

from playwright.sync_api import Playwright, expect, Page


def test_buttons(formy_setup):
    page = formy_setup
    page.get_by_role("link", name="Buttons").click()

    expect(page.get_by_role("button", name="Primary")).to_be_visible()
    # click all buttons
    for index in range(page.get_by_role("button").count()-1):
        page.get_by_role("button").nth(index).click()
    # page.get_by_role("button", name="Primary").click()
    page.locator("#btnGroupDrop1").click()
    page.locator(".dropdown-item").filter(has_text="Dropdown link 1").click()
    page.locator("#btnGroupDrop1").click()
    page.locator(".dropdown-item").filter(has_text="Dropdown link 1").click()







