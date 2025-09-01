class Scroll:

    def __init__(self, page, expect):
        self.page = page
        self.expect = expect

    def actions(self):
        self.page.get_by_placeholder("Full name").scroll_into_view_if_needed()
        self.page.get_by_placeholder("Full name").fill("Wasim Shaikh")
        self.expect(self.page.get_by_placeholder("Full name")).to_have_value("Wasim Shaikh")
        self.page.get_by_placeholder("MM/DD/YYYY").fill("02/11/1996")
        self.expect(self.page.get_by_placeholder("MM/DD/YYYY")).not_to_be_empty()

    def validate_module_page(self, module):
        self.expect(self.page.locator("h1")).to_have_text(module)