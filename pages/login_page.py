from locators.login_locator import LoginLocator

class LoginPage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(
            "https://nusacodes.com/login",
            wait_until="domcontentloaded",
            timeout=60000
        )

    def input_email(self, email):
        self.page.locator(LoginLocator.EMAIL).fill(email)

    def input_password(self, password):
        self.page.locator(LoginLocator.PASSWORD).fill(password)

    def click_login(self):
        self.page.locator(LoginLocator.LOGIN_BUTTON).click()