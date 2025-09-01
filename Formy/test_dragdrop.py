from playwright.sync_api import expect
from page_object.home_page import Home

def test_drag_drop(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    page.get_by_role("link", name="Drag and Drop").click()

    expect(page.locator("h1")).to_have_text("Drag the image into the box")

    source = page.locator("div#image")
    destination = page.locator("div#box")
    source.drag_to(destination)
    homepage.redirect()
