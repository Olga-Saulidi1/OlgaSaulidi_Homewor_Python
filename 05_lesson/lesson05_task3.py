from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service 
from webdriver_manager.firefox import DriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()

# Открыть баузер и перейти на страницу
driver.get("http://the-internet.herokuapp.com/inputs")
sleep(2)

# Найти поле ввести слово, удалить слово, ввести другое слово
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input_field.send_keys("Sky")
print("Введен текст: Sky")
sleep(1)

input_field.clear()
print("Поле очищено")
sleep(1)

input_field.send_keys("Pro")
print("Введен текст: Pro")
sleep(2)

# Закрыть браузер
driver.quit()
    

