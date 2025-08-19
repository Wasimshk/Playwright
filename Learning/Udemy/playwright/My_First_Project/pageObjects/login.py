class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self, userdata):
        Email = userdata['userEmail']
        Password = userdata['userPassword']
        self.page.goto("https://rahulshettyacademy.com/client")
        self.page.get_by_placeholder("email@example.com").fill(Email)
        self.page.get_by_placeholder("enter your passsword").fill(Password)
        self.page.get_by_role("button", name="Login").click()
