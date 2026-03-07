from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Открыть баузер
driver.get("http://uitestingplayground.com/ajax")

# Кликнуть на синюю кнопку
blue_button = driver.find_element(By.ID, "ajaxButton")
blue_button.click()
print("Клик на синюю кнопку выполнен")

wait = WebDriverWait(driver, 20)

# Вывод текста из зеленой плашки
green_banner = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content p.bg-success")
        )
)
print(green_banner.text)

driver.quit()