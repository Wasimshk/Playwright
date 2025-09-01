class Enabledisable:

    def __init__(self, page, expect):
        self.page = page
        self.expect = expect

    def actions(self):
        self.expect(self.page.get_by_placeholder("Disabled input here...")).to_be_disabled()
        self.expect(self.page.get_by_placeholder("Disabled input here...")).not_to_be_editable()
        self.expect(self.page.locator("#input")).to_be_enabled()
        self.expect(self.page.locator("#input")).to_be_editable()
        self.page.locator("#input").fill("Wasim Shaikh")
        self.expect(self.page.locator("#input")).to_have_value("Wasim Shaikh")

    def validate_module_page(self, module):
        self.expect(self.page.locator("h1")).to_have_text(module)