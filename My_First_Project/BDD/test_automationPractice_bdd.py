from pytest_bdd import given, when, then, parsers, scenarios
from playwright.sync_api import Page, expect

scenarios("features\\automationPractice.feature")

@given("user is on the login page")
def goto_login_page(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

@when("user enters valid username and password")
def enter_login_details(page:Page):
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()

@when("clicks on the login button")
def click_login(page):
    page.get_by_role("button", name="Sign In").click()

@then("the user should be redirected to the dashboard")
def validate_dashboard(page:Page):
    expect(page.locator("h1")).to_contain_text("Shop Name")


# --- Scenario Outline (with parameterized steps) ---
@given("user is on the login page")
def goto_login_page(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

@when(parsers.parse("user enters invalid {username} or {password}"))
def enter_invalid_login_details(page:Page, username, password):
    page.get_by_label("Username:").fill(username)
    page.get_by_label("Password:").fill(password)
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()

@when("clicks on the login button")
def click_login(page):
    page.get_by_role("button", name="Sign In").click()

@then("user should see an error message")
def valid_error_message(page):
    expect(page.locator(".alert-danger.alert")).to_have_text("Incorrect username/password.")

# mouse hover
@given("User is on the automation practice page")
def navigate_to_automation_practice_page(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

@when("the user hover the mouse to Mouse hover button")
def mouse_hover(page):
    page.get_by_role("button", name="Mouse Hover").hover()

@then("drop down options appear")
def validate_dropdown(page:Page):
    expect(page.locator(".mouse-hover-content")).to_be_visible()

@then("user click on the top option")
def select_dropdown_option(page):
    page.get_by_role("link", name="Top").click()


# alert box
@given("User is on the automation practice page")
def navigate_to_automation_practice_page(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

@when("user click on the confirm button and accept dialog")
def click_confirm_button_and_accept_dialog(page:Page):
    page.on("dialog", lambda dialog_event_argument: dialog_event_argument.accept())
    page.get_by_role("button", name="Confirm").click()

@then("user cofirms the dialog is disappeared")
def validate_the_dialog_is_handled(page):
    expect(page).to_have_title("Practice Page")