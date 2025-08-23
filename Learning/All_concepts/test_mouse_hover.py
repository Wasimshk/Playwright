import pytest
from playwright.sync_api import Page

@pytest.mark.ui
def test_mouse_hover(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.get_by_role("button", name="Mouse Hover").hover()
    page.get_by_role("link", name="Top").click()