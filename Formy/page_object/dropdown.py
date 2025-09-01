class Dropdown:

    def __init__(self, page, expect):
        self.page = page
        self.expect = expect

    def actions(self):
        self.page.locator("#dropdownMenuButton").click()
        self.page.locator('[class="dropdown-menu show"] > a').filter(has_text="Checkbox").click()

    def validate_module_page(self, module):
        self.expect(self.page.locator("h1")).to_have_text(module)