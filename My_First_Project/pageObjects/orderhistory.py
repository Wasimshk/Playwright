class OrderHistoryPage:
    def __init__(self, page):
        self.page = page

    def validate_order_id(self, orderID):
        productRow = self.page.locator("tr").filter(has_text=orderID)
        productRow.get_by_role("button", name="View").click()