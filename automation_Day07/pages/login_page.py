
class LoginPage:

    def __init__(self, page):
        self.page = page

        # locators
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        # shared error box — assert exact text in the test
        self.error_message = page.locator("[data-test='error']")

    def enter_username(self, username):
        self.username.fill(username)

    def enter_password(self, password):
        self.password.fill(password)

    def click_button(self):
        self.login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_button()