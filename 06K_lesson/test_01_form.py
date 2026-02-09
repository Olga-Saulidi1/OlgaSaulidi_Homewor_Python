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
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.ID, "email").send_keys("test@skypro.com")
        driver.find_element(By.ID, "phone").send_keys("+7985899998787")
        driver.find_element(By.ID, "zip-code").clear()
        driver.find_element(By.ID, "city").send_keys("Москва")
        driver.find_element(By.ID, "country").send_keys("Россия")
        driver.find_element(By.ID, "job-position").send_keys("QA")
        driver.find_element(By.ID, "company").send_keys("SkyPro")
        
        driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        
        WebDriverWait(driver, 10).until(
            lambda d: "is-invalid" in d.find_element(By.ID, "zip-code").get_attribute("class")
        )
        
        zip_code_field = driver.find_element(By.ID, "zip-code")
        assert "is-invalid" in zip_code_field.get_attribute("class"), "Zip code не подсвечен красным"
        
        green_fields = ["first-name", "last-name", "address", "email", 
                       "phone", "city", "country", "job-position", "company"]
        
        for field_id in green_fields:
            field = driver.find_element(By.ID, field_id)
            assert "is-valid" in field.get_attribute("class"), f"Поле {field_id} не подсвечено зеленым"
        
        print("Все проверки пройдены успешно!")
        
    finally:
        driver.quit()

