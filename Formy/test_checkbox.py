from time import sleep
from playwright.sync_api import expect
from page_object.home_page import Home


def test_checkbox(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    
    page.get_by_role("link", name="Checkbox").click()

    expect(page.locator("h1")).to_have_text("Checkboxes")
    for i in range(1, 4):
        page.locator(f"#checkbox-{i}").check()
        expect(page.locator(f"#checkbox-{i}")).to_be_checked()
        page.locator(f"#checkbox-{i}").uncheck()
        expect(page.locator(f"#checkbox-{i}")).not_to_be_checked()

    homepage.redirect()
