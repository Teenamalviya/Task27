from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.config import BasePage as BP

class Home_Page:
    def __init__(self, driver):
        self.driver = driver

    cls_text = (By.XPATH, '//*[@id="root"]/nav/h1')
    account_name = (By.CLASS_NAME, "profileIcon")
    logout_text = (By.XPATH, '//*[@id="root"]/nav/div/div/div/div/button[2]')

    def entering_the_home_page(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.cls_text))

    def do_logout(self):
        self.driver.find_element(self.account_name)
        self.driver.find_element(self.logout_text)

    def refresh(self):
        self.driver.refresh()

