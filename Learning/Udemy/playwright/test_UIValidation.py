import time
from sys import exception

from playwright.sync_api import Page, expect
from win32api import Sleep


def test_ui_validation(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    # filter out the unique element dynamically by scanning the common locator
    # Note - the filter will work only on locator() method not on get_by_label() or other methods
    SamsungElem = page.locator("app-card").filter(has_text="Samsung Note 8")
    SamsungElem.get_by_role("button").click()
    NokiaElem = page.locator("app-card").filter(has_text="Nokia Edge")
    NokiaElem.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator("div.media")).to_have_count(2)
    expect(page.get_by_text("Samsung")).to_have_text("Samsung Note 8")
    expect(page.get_by_role("link", name="Nokia Edge")).to_have_text("Nokia Edge")
    time.sleep(5)

def test_child_window_validation(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as new_page_info:
        page.locator(".blinkingText").click()
        chilpage = new_page_info.value
        text = chilpage.locator(".red").text_content()
        # playwright exception handling
        expect(chilpage.locator(".red")).to_contain_text("mentor@rahulshettyacademy.com")

        print(text)
        split_text1 = text.split("at")
        print(split_text1[1])
        split_text2 = split_text1[1].split("with")
        print(split_text2[0])
        email = split_text2[0].strip()
        print(email)
        # pyTest exception handling
        assert email == "mentor@rahulshettyacademy.com"
        # try:
        #     if email != "mentor@rahulshettyacademy.co":
        #         raise Exception("email does not match")
        # except Exception as e:
        #     print(e)