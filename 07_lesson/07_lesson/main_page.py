from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.backpack = (By.ID, 'add-to-cart-sauce-labs-backpack')
        self.tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_button = (By.CSS_SELECTOR, '.shopping_cart_link')

    def add_backpack(self):
        self.driver.find_element(*self.backpack).click()

    def add_tshirt(self):
        self.driver.find_element(*self.tshirt).click()

    def add_onesie(self):
        self.driver.find_element(*self.onesie).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()