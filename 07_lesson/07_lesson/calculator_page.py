from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, '#delay')
        self.result_field = (By.CSS_SELECTOR, '.screen')
        self.buttons = {
            '7': (By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']"),
            '+': (By.XPATH, "//span[@class='operator btn btn-outline-success' and text()='+']"),
            '8': (By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']"),
            '=': (By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']")
        }
        self.driver.implicitly_wait(10) 

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay: int):
        delay_input = self.driver.find_element(*self.delay_input)
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_button(self, button_name: str):
        button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.buttons[button_name])
        )
        button.click()
    def get_result(self) -> str:
        return self.driver.find_element(*self.result_field).text