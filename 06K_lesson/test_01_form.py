from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "first-name"))
        )
        
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "zip-code").clear()
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")
        
        driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        
        WebDriverWait(driver, 10).until(
            lambda d: "is-invalid" in d.find_element(By.NAME, "zip-code").get_attribute("class")
        )        
        zip_code_field = driver.find_element(By.NAME, "zip-code")
        assert "is-invalid" in zip_code_field.get_attribute("class"), "Zip code не подсвечен красным"
        
        green_fields = ["first-name", "last-name", "address", "email",
                        "phone", "city", "country", "job-position", "company"]        
        for field_id in green_fields:
            field = driver.find_element(By.NAME, field_id)
            assert "is-valid" in field.get_attribute("class"), f"Поле {field_id} не подсвечено зеленым"        
        print("Все проверки пройдены успешно!")
    finally: driver.quit()