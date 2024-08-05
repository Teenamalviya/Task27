import pytest
from selenium import webdriver
from configuration import config as path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

driver = None
driver_path = ("C:\z.selenium drivers\chromedriver-win64\chromedriver.exe")
orange_url = ("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@pytest.fixture(scope="class")
def chrome_driver(request):

    # Setup Chrome driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(orange_url)
    request.cls.driver = orange_url

    yield driver
    # Teardown Chrome driver
    driver.quit()

