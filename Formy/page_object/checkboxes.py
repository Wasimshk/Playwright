class Checkboxes:

    def __init__(self, page, expect):
        self.page = page
        self.expect = expect

    def actions(self):
        for i in range(1, 4):
            self.page.locator(f"#checkbox-{i}").check()
            self.expect(self.page.locator(f"#checkbox-{i}")).to_be_checked()
            self.page.locator(f"#checkbox-{i}").uncheck()
            self.expect(self.page.locator(f"#checkbox-{i}")).not_to_be_checked()

    def validate_module_page(self, module):
        self.expect(self.page.locator("h1")).to_have_text(module)