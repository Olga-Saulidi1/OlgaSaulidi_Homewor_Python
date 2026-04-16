from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_full_purchase(browser):
    # Авторизация
    login_page = LoginPage(browser)
    login_page.open()
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login()

    # Добавление товаров
    main_page = MainPage(browser)
    main_page.add_backpack()
    main_page.add_tshirt()
    main_page.add_onesie()
    main_page.go_to_cart()

    # Переход к оформлению заказа
    cart_page = CartPage(browser)
    cart_page.click_checkout()

    # Оформление заказа
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_first_name('Ольга')
    checkout_page.fill_last_name('Саулиди')
    checkout_page.fill_postal_code('344092')
    checkout_page.click_continue()

    # Проверка итоговой суммы
    total_amount = checkout_page.get_total_amount()
    assert total_amount == '$58.29'