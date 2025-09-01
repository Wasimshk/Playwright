from playwright.sync_api import Page, expect


def test_drag_and_drop(page: Page):
    page.goto("https://formy-project.herokuapp.com/dragdrop")  # Replace with your actual URL

    expect(page.locator("h1")).to_have_text("Drag the image into the box")

    source = page.locator("div#image")
    destination = page.locator("div#box")
    source.drag_to(destination)