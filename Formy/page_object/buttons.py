class Buttons:

    def __init__(self, page, expect):
        self.page = page
        self.expect = expect

    def actions(self):
        # click all buttons
        for index in range(self.page.get_by_role("button").count() - 1):
            self.page.get_by_role("button").nth(index).click()
        # self.page.get_by_role("button", name="Primary").click()
        self.page.locator("#btnGroupDrop1").click()
        self.page.locator(".dropdown-item").filter(has_text="Dropdown link 1").click()
        self.page.locator("#btnGroupDrop1").click()
        self.page.locator(".dropdown-item").filter(has_text="Dropdown link 1").click()

    def validate_module_page(self):
        self.expect(self.page.get_by_role("button", name="Primary")).to_be_visible()