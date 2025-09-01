from playwright.sync_api import expect
from page_object.home_page import Home

def test_drag_drop(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    module = "Drag and Drop"
    homepage.open_module(module)
    
    # Note: No page object for drag and drop - actions performed directly
    # Validate page
    expect(page.locator("h1")).to_have_text("Drag the image into the box")
    
    # Perform drag and drop action
    source = page.locator("div#image")
    destination = page.locator("div#box")
    source.drag_to(destination)
    homepage.redirect()
