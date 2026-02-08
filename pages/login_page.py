from locators.login_locators import LoginLocators

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*LoginLocators.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginLocators.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginLocators.LOGIN_BTN).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
