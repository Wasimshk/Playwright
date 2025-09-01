class Modal:

    def __init__(self, page, expect):
        self.page = page
        self.expect = expect

    def actions(self):
        self.page.locator("#modal-button").click()
        self.expect(self.page.locator(".modal-title")).to_be_visible()
        # self.page.locator("button:has-text('Close')").click()
        self.page.locator("button").filter(has_text="Close").click()
        self.expect(self.page.locator(".modal-title")).not_to_be_visible()

    def validate_module_page(self, module):
        self.expect(self.page.locator("h1")).to_have_text(module)