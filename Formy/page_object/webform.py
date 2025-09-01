class Webform:

    def __init__(self, page, expect):
        self.page = page
        self.expect = expect

    def actions(self):
        self.page.get_by_label("First name").fill("Wasim")
        self.page.get_by_label("Last name").fill("Shaikh")
        self.page.get_by_label("Job title").fill("SDET")
        self.page.locator("#radio-button-3").check()
        self.expect(self.page.locator("#radio-button-3")).to_be_checked()
        self.page.locator("#checkbox-1").check()
        self.expect(self.page.locator("#checkbox-1")).to_be_checked()
        self.page.locator("#select-menu").select_option("3")
        self.page.get_by_placeholder("mm/dd/yyyy").fill("02/11/1996")
        self.expect(self.page.get_by_placeholder("mm/dd/yyyy")).not_to_be_empty()
        self.page.get_by_role("button", name="Submit").click()

    def validate_module_page(self, module):
        self.expect(self.page.locator("h1")).to_have_text(module)