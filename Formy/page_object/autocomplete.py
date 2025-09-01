class Autocomplete:
    def __init__(self, page, expect):
        self.page = page
        self.expect = expect

    def actions(self):
        self.page.get_by_placeholder("Enter address").fill("lane 4")
        self.page.locator("#street_number").fill("block 4")
        self.page.get_by_placeholder("Street address 2").fill("area 4")
        self.page.get_by_placeholder("City").fill("Pune")
        self.page.get_by_placeholder("State").fill("Maharashtra")
        self.page.get_by_placeholder("Zip code").fill("411001")
        self.page.get_by_placeholder("Country").fill("India")

    def validate_module_page(self, module):
        self.expect(self.page.locator("h1")).to_have_text(module)