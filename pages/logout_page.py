from locators.logout_locator import LogoutLocator

class LogoutPage:

    def __init__(self, page):
        self.page = page

    def click_logout(self):
        self.page.locator(LogoutLocator.LOGOUT_BUTTON).click()