import pytest
from selenium import webdriver
from shop.shop_page import ShopPage
from shop.order_page import OrderPage
from shop.cart_page import CartPage
from shop.data_page import DataPage
from shop.result_page import ResultPage


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_total(driver):
    shop_page = ShopPage(driver)
    shop_page.get_authorization()

    order_page = OrderPage(driver)
    order_page.do_order()

    cart_page = CartPage(driver)
    cart_page.check_orders()

    data_page = DataPage(driver)
    data_page.set_data()

    result_page = ResultPage(driver)
    total = result_page.get_total()
    assert total.replace('Total: $', '') == '58.29'
