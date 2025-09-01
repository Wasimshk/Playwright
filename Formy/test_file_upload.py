from playwright.sync_api import expect
from page_object.home_page import Home

def test_file_upload(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()

    page.get_by_role("link", name="File Upload").click()
    expect(page.locator("h1")).to_have_text("File upload")

    filepath = "C:\WasimShaikh\Projects\Playwright\Formy\formy_homepage_content.txt"
    page.get_by_placeholder("Choose a file...").fill(filepath)
    expect(page.get_by_placeholder("Choose a file...")).not_to_be_empty()
    homepage.redirect()