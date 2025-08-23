import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
def test_child_window(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as child_window:
        page.locator(".blinkingText").click()
        child_page = child_window.value
        # direct assertion
        expect(child_page.locator("p.red")).to_contain_text("mentor@rahulshettyacademy.com")

        # extract email and assert
        text = child_page.locator("p.red").text_content()

        # one way
        words = text.split("at ")
        word_list = words[1].split()
        email = word_list[0]
        print("Email extracted through split method: ", email)
        assert email == "mentor@rahulshettyacademy.com"

        # other way
        email = None
        words = text.split()
        for word in words:
            if "@" in word:
                email = word

        print("Email extracted through loop: ", email)
        assert email == "mentor@rahulshettyacademy.com"