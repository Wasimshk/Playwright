class Radio:

    def __init__(self, page, expect):
        self.page = page
        self.expect = expect

    def actions(self):
        # page.get_by_role("radio", name="Radio button 1").click()
        self.expect(self.page.get_by_role("radio", name="Radio button 1")).to_be_checked()

        self.page.locator('[value="option2"]').click()
        self.expect(self.page.locator('[value="option2"]')).to_be_checked()

        # using xpath and sibling approach
        # self.page.locator(xpath='//label[@class="form-check-label"]/preceding-sibling::input[@value="option3"]').click()
        # self.expect(self.page.locator(xpath='//input[@value="option3"]')).to_be_checked()

    def validate_module_page(self, module):
        self.expect(self.page.locator("h1")).to_have_text(module)