from playwright.sync_api import expect


class OrderSummaryPage:
    def __init__(self, page):
        self.page = page

    def view_order_Summary(self):
        expect(self.page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")