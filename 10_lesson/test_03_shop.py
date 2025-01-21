import pytest
from selenium import webdriver
from shop.shop_page import ShopPage
from shop.order_page import OrderPage
from shop.cart_page import CartPage
from shop.data_page import DataPage
from shop.result_page import ResultPage
import allure


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест на прохождение флоу покупки в интернет-магазине")
@allure.description("Прохождение покупки в несколько этапов(страниц сайта)")
@allure.feature("Покупка")
@allure.severity(allure.severity_level.NORMAL)
def test_total(driver):
    with allure.step("Заходим на первую страницу сайта и авторизовываемся"):
        shop_page = ShopPage(driver)
        shop_page.get_authorization()

    with allure.step("Выбор товара, складываем в корзину позиции"):
        order_page = OrderPage(driver)
        order_page.do_order()

    with allure.step("Переход в корзину, проверка товаров"):
        cart_page = CartPage(driver)
        cart_page.check_orders()

    with allure.step("Заполняем данные для заказа"):
        data_page = DataPage(driver)
        data_page.set_data()

    with allure.step("Переход на итоговую страницу сайта, проверяем сумму заказа"):
        result_page = ResultPage(driver)
        total = result_page.get_total()
        assert total.replace('Total: $', '') == '58.29'
