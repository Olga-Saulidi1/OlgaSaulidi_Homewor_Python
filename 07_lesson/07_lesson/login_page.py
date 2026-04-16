from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.username_input = (By.ID, 'user-name')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    def open(self):
        self.driver.get("https://www.saucedemo.com")

    def enter_username(self, username: str):
        self.driver.find_element(*self.username_input).send_keys("standard_user")

    def enter_password(self, password: str):
        self.driver.find_element(*self.password_input).send_keys("secret_sauce")

    def click_login(self):
        self.driver.find_element(*self.login_button).click()