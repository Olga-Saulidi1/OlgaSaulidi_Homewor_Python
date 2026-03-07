from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo_purchase():
    driver = webdriver.Firefox()
    
    try:
        driver.get("https://www.saucedemo.com/")
        
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cart_contents_container"))
        )
        
        driver.find_element(By.ID, "checkout").click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkout_info_container"))
        )
        
        driver.find_element(By.ID, "first-name").send_keys("Ольга")
        driver.find_element(By.ID, "last-name").send_keys("Саулиди")
        driver.find_element(By.ID, "postal-code").send_keys("344092")
        driver.find_element(By.ID, "continue").click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        
        total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        
        assert total_text == "Total: $58.29", f"Итоговая сумма неверна: {total_text}"
        
        print(f"Тест пройден! Итоговая сумма: {total_text}")
        
    finally:
        driver.quit()
