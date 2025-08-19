from Learning.Udemy.playwright.My_First_Project.pageObjects.dashboard import DashBoardPage


class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self, userdata):
        Email = userdata['userEmail']
        Password = userdata['userPassword']
        self.page.get_by_placeholder("email@example.com").fill(Email)
        self.page.get_by_placeholder("enter your passsword").fill(Password)
        self.page.get_by_role("button", name="Login").click()

        # # we are sure that the after login it will open the dashboard page hence we can call the dashboard object here as well
        # # create dashboard page object
        # dashboardPageObj = DashBoardPage(self.page)
        # return dashboardPageObj
