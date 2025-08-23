import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
def test_visiblity(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    expect(page.get_by_placeholder("Hide/Show Example")).not_to_be_hidden()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).not_to_be_visible()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()