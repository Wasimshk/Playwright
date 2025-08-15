import time
from time import sleep

from playwright.sync_api import Page, expect


def test_visibility_checks(page:Page):
    # hide/display and placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    # alertboxes
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()


    # another way for alert box
    def handle_dialog(dialog):
        dialog.accept()
    page.on("dialog", handle_dialog)
    page.get_by_role("button", name="Confirm").click()

    # mouse Hover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()

    #framehandling
    frame_page = page.frame_locator("#courses-iframe")
    frame_page.get_by_role("link", name="Job Support").click()
    expect(frame_page.locator("h1")).to_contain_text("Job Support")


    # handle table
    # check the price of rice is equal to 37
    # identify the price column
    # identify the row
    # exact price of the rice

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    priceColumnValue = None
    for i in range(page.locator("th").count()):
        if page.locator("th").nth(i).filter(has_text="Price").count()>0:
            priceColumnValue = i
            print(str(1+priceColumnValue) + " Column is the price column")
            break
    riceRow = page.locator("tr").filter(has_text="Rice")
    ricePrice = riceRow.locator("td").nth(priceColumnValue)
    print(f"price of the rice is {ricePrice.text_content()}")
    expect(ricePrice).to_have_text("37")