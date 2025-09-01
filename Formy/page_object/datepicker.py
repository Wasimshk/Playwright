class Datepicker:

    def __init__(self, page, expect):
        self.page = page
        self.expect = expect

    def actions(self, birthdate):
        self.page.get_by_placeholder("mm/dd/yyyy").fill(birthdate)
        self.expect(self.page.get_by_placeholder("mm/dd/yyyy")).not_to_be_empty()
        self.expect(self.page.get_by_placeholder("mm/dd/yyyy")).to_have_value(birthdate)

    def validate_module_page(self, module):
        self.expect(self.page.locator("h1")).to_have_text(module)