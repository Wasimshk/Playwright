# test_loginwithmcp_playwright.py
# Playwright test for login and product verification

import pytest
from playwright.sync_api import sync_playwright, expect

def test_login_and_verify_iphone_x():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        page.fill('input#username', 'rahulshettyacademy')
        page.fill('input#password', 'learning')
        page.check('input[type="checkbox"]')
        page.click('input#signInBtn')
        page.wait_for_url("**/angularpractice/shop", timeout=10000)
        # Verify iphone X is present
        assert page.locator("//h4[contains(text(), 'iphone X')]").is_visible(), "iphone X product not found on the shop page!"
        browser.close()
