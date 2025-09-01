class Fileupload:

    def __init__(self, page, expect):
        self.page = page
        self.expect = expect

    def actions(self):
        filepath = "C:/WasimShaikh/Projects/Playwright/Formy/webscraping/formy_homepage_content.txt"
        self.page.get_by_placeholder("Choose a file...").fill(filepath)
        self.expect(self.page.get_by_placeholder("Choose a file...")).not_to_be_empty()

    def validate_module_page(self, module):
        self.expect(self.page.locator("h1")).to_have_text(module)