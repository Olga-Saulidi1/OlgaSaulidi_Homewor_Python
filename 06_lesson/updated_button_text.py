from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Открыть баузер
driver.get("http://uitestingplayground.com/textinput")

# Написать текст и кликнуть на синюю кнопку
input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

blue_button = driver.find_element(By.ID, "updatingButton")
blue_button.click()

print ("Клик на синюю кнопку")

updated_button_text = blue_button.text
print(updated_button_text)

driver.quit()