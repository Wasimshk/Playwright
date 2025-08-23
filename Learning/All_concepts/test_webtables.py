import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
def test_webtables(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    columnheader = page.locator("th[role='columnheader']")
    colValue = None
    for i in range(columnheader.count()):
        if columnheader.nth(i).filter(has_text="Price").count()>0:
            colValue = i
            print(f"Price Column Value is: {colValue}")
            break

    riceRow = page.locator("tr").filter(has_text="Rice")
    print("rice row: ", riceRow)
    expect(riceRow.locator("td").nth(colValue)).to_have_text("37")