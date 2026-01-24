from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# Открыть баузер
driver.get("http://uitestingplayground.com/classattr")
sleep(5)

# Кликнуть на синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
blue_button.click()
print("Клик на синюю кнопку выполнен")
sleep(3)

