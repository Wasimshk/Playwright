# this code is generator from codegen
import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test_codegen(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("rahulshettyacademy")
    page.get_by_role("textbox", name="Username:").press("Tab")
    page.get_by_role("textbox", name="Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox", name="I Agree to the terms and").check()
    page.locator("label:nth-child(2) > .checkmark").click()
    page.get_by_role("button", name="Okay").click()
    page.get_by_role("button", name="Sign In").click()
    page.locator("app-card").filter(has_text="Samsung Note 8 $24.99 Lorem").get_by_role("button").click()
    page.locator("app-card").filter(has_text="Nokia Edge $24.99 Lorem ipsum").get_by_role("button").click()
    page.get_by_text("Checkout ( 2 ) (current)").click()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_role("textbox", name="Please choose your delivery").click()
    page.get_by_role("textbox", name="Please choose your delivery").fill("india")
    page.get_by_text("India").click()
    page.get_by_text("I agree with the term &").click()
    page.get_by_role("button", name="Purchase").click()
    page.get_by_role("link", name="close").click()

    # ---------------------
    context.close()
    browser.close()

# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://rahulshettyacademy.com/loginpagePractise/")
#     page.get_by_role("textbox", name="Username:").click()
#     page.get_by_role("textbox", name="Username:").fill("rahulshettyacademy")
#     page.get_by_role("textbox", name="Username:").press("Tab")
#     page.get_by_role("textbox", name="Password:").fill("learning")
#     page.get_by_role("combobox").select_option("teach")
#     page.get_by_role("checkbox", name="I Agree to the terms and").check()
#     page.locator("label:nth-child(2) > .checkmark").click()
#     page.get_by_role("button", name="Okay").click()
#     page.get_by_role("button", name="Sign In").click()
#     page.locator("app-card").filter(has_text="Samsung Note 8 $24.99 Lorem").get_by_role("button").click()
#     page.locator("app-card").filter(has_text="Nokia Edge $24.99 Lorem ipsum").get_by_role("button").click()
#     page.get_by_text("Checkout ( 2 ) (current)").click()
#     page.get_by_role("button", name="Checkout").click()
#     page.get_by_role("textbox", name="Please choose your delivery").click()
#     page.get_by_role("textbox", name="Please choose your delivery").fill("india")
#     page.get_by_text("India").click()
#     page.get_by_text("I agree with the term &").click()
#     page.get_by_role("button", name="Purchase").click()
#     page.get_by_role("link", name="close").click()
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)
