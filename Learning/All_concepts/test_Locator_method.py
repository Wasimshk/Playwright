

# all posible locator with filters will be here

'''
Playwright's Selector Engines
Unlike plain CSS, Playwright combines multiple engines:
    CSS: "button.my-class"
    Text: "text='Submit'" – elements containing text.
    Combination: "button:has-text('Submit')"
    XPath: "xpath=//button[@id='login']"
    Other Pseudo-classes:
        :has() → matches elements containing other elements.
        :nth-match() → select nth occurrence.
        :visible → selects visible elements only.
'''

def test_locator_methods(page):
    page.locator("button:has-text('Close')")
    page.locator("button").filter(has_text="Close", has=page.locator("svg.close-icon")).click()
# Cheat Sheet
# 1. Basic Locators
    page.locator("button")                     # CSS selector
    page.locator("text='Login'")               # Text selector
    page.locator("xpath=//button[@id='login']")# XPath selector
    page.locator("role=button[name='Login']")  # ARIA role selector
# 2. Chaining and Filtering
# .filter()
    page.locator("button").filter(has_text="Close").click()
# Filters elements that contain exact text.
    page.locator("div").filter(has=page.locator("button")).click()
# Filters elements that contain another element.
# 3. Element Position
# .nth(index)
    page.locator("button").nth(0).click()  # First button
    page.locator("button").nth(2).click()  # Third button
# .first() and .last()
    page.locator("button").first.click()
    page.locator("button").last.click()
# 4. State Filters
# .is_visible(), .is_enabled(), .is_checked()
    if page.locator("button#submit").is_enabled():
        page.locator("button#submit").click()
# Pseudo-Class Selectors
    page.locator("button:visible").click()
    page.locator("input:checked")
# 5. Chaining Locators
# .locator() Inside Another Locator
    modal = page.locator(".modal")
    modal.locator("button:has-text('Close')").click()
# Finds element within a specific parent.
# 6. Combining Filters
    page.locator("button").filter(
        has_text="Save",
        has=page.locator("svg.save-icon")
    ).click()
# Matches a button that has both text and contains an icon.
# 7. Wait for Elements
    page.locator("button:has-text('Login')").wait_for(state="visible")
    # States: "visible", "hidden", "attached", "detached"
# 8. Assertions
#     from playwright.sync_api import expect
    # expect(page.locator("h1")).to_have_text("Welcome")
    # expect(page.locator("input#username")).to_be_visible()
    # Best Practice
    # Prefer CSS + text filters for performance.
    # Use .filter() for readability when chaining conditions.
    # Avoid XPath unless necessary.

