from time import sleep

from playwright.sync_api import Page


def test_UI_validation(page:Page):
    page.goto("https://selectorshub.com/xpath-practice-page/")
    page.locator("select.dt-input").select_option("25")
    page.locator("input.dt-input").fill("India")
    tableContent = page.locator("tbody.row-striping").text_content()
    print(tableContent)
    sleep(5)