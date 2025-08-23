import pytest
from playwright.sync_api import Page, expect


@pytest.mark.logintest
def test_login(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()

@pytest.mark.logintest
def test_login_invalid_creds(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("wrongusername")
    page.get_by_label("Password:").fill("wrongpasswork")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.locator(".alert-danger.alert")).to_have_text("Incorrect username/password.")