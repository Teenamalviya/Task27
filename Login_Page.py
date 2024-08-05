from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.config import BasePage
from page.Home_Page import Home_Page

class Login_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.username = (By.NAME,'username')
        self.password = (By.NAME, 'password')
        self.login_btn = (By.XPATH, '//button[@type="submit"]')

    # for Login
    def click_login(self, username, passcode):
        BasePage.do_send_keys(self, self.username, username)
        BasePage.do_send_keys(self, self.password, passcode)
        BasePage.do_clicks(self, self.login_btn)
        return Home_Page(self.driver)
