import pytest
from playwright.sync_api import Page, expect

# alert box
@pytest.mark.ui
def test_alertbox(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog_event_argument: dialog_event_argument.accept())
    page.get_by_role("button", name="Confirm").click()

# frame\iframe
@pytest.mark.ui
def test_frame(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    frame_page = page.frame_locator("#courses-iframe")
    frame_page.get_by_role("link", name="All Access Plan").click()
    expect(frame_page.locator("body")).to_contain_text("Happy Subscibers!")