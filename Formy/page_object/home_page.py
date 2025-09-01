
class Home:

    def __init__(self, page, expect):
        self.page = page
        self.expect = expect

    def navigate(self):
        """open home page and validate"""
        self.page.goto("https://formy-project.herokuapp.com/")
        self.expect(self.page.locator("h1")).to_have_text("Welcome to Formy")

    def redirect(self):
        """click Formy logo and validation the redirection to home page"""
        self.page.locator("#logo").click()
        # validate home page
        self.expect(self.page.locator("h1")).to_have_text("Welcome to Formy")

    def open_module(self, module):
        self.page.get_by_role("link", name=module).click()