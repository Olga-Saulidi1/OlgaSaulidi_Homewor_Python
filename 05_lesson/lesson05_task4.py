from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service 
from webdriver_manager.firefox import DriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

# Открыть баузер и перейти на страницу
driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

# ВВести логин и пароль
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")
print("Введен логин")
sleep(2)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")
print("Введен пароль")
sleep(2)

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
print("Кнопка Login нажата")
sleep(2)

# Вывести текст с зеленой плашки в консоль
flash_element = driver.find_element(By.CSS_SELECTOR, "div.flash.flash.success")
print(flash_element.text)

# Закрыть браузер
driver.quit()