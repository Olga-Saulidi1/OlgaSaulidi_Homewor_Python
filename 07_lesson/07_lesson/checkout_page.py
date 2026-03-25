from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.CSS_SELECTOR, '[data-test="continue"]')
        self.total_amount = (By.CSS_SELECTOR, '[data-test="total-label"]')

    def fill_first_name(self, first_name: str):
        self.driver.find_element(*self.first_name).send_keys(first_name)

    def fill_last_name(self, last_name: str):
        self.driver.find_element(*self.last_name).send_keys(last_name)

    def fill_postal_code(self, postal_code: str):
        self.driver.find_element(*self.postal_code).send_keys(postal_code)

    def click_continue(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()
      
    def get_total_amount(self) -> str:
        element = WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located(self.total_amount)
    )
        return element.text.replace('Total: ', '').strip()