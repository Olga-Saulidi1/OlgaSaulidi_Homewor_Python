from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
driver.maximize_window()

# Ждем загрузки всех картинок
wait = WebDriverWait(driver, 20)

wait.until(
    lambda d: len([img for img in d.find_elements(By.TAG_NAME, "img") 
                 if "loading.gif" not in img.get_attribute("src")]) >= 4
)
print("✓ Все картинки загрузились")

# Ищем 3-ю картинку и выводим в консоль
third_image = driver.find_element(By.ID, "award")
image_src_value = third_image.get_attribute("src")

print(image_src_value)

driver.quit()