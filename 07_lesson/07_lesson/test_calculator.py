from selenium import webdriver
from calculator_page import CalculatorPage
import time
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator_addition(browser):
    calculator = CalculatorPage(browser)
    calculator.open()
    calculator.set_delay(45)
    
    calculator.click_button('7')
    time.sleep(1)
    calculator.click_button('+')
    time.sleep(1)
    calculator.click_button('8')
    time.sleep(1)
    
    time.sleep(2)  
    calculator.click_button('=')
    
    time.sleep(45) 
    
    result = calculator.get_result()
    assert result == '15'