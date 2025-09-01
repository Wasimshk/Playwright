class Windowhandle:

    def __init__(self, page, expect):
        self.page = page
        self.expect = expect

    def child_window_action(self):
        with self.page.expect_popup() as childwindow:
            self.page.locator("#new-tab-button").click()
            childpage = childwindow.value
            self.expect(childpage.locator("h1")).to_have_text("Welcome to Formy")
            childpage.get_by_role("link", name="Checkbox").click()
            self.expect(childpage.locator("h1")).to_have_text("Checkboxes")

    def dialog_action(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.locator("#alert-button").click()

    def validate_module_page(self, module):
        self.expect(self.page.locator("h1")).to_have_text(module)