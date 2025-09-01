from playwright.sync_api import expect
from page_object.home_page import Home

def test_child_window(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    page.get_by_role("link", name="Switch Window").click()
    expect(page.locator("h1")).to_have_text("Switch Window")

    with page.expect_popup() as childwindow:
        page.locator("#new-tab-button").click()
        childpage = childwindow.value
        expect(childpage.locator("h1")).to_have_text("Welcome to Formy")
        childpage.get_by_role("link", name="Checkbox").click()
        expect(childpage.locator("h1")).to_have_text("Checkboxes")
    homepage.redirect()


def test_dialog_box(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    page.get_by_role("link", name="Switch Window").click()
    expect(page.locator("h1")).to_have_text("Switch Window")

    page.on("dialog", lambda dialog:dialog.accept())
    page.locator("#alert-button").click()
    homepage.redirect()