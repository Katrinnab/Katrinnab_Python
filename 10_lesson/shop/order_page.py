from selenium.webdriver.common.by import By
import allure

orders_list = ['#add-to-cart-sauce-labs-backpack',
               '#add-to-cart-sauce-labs-bolt-t-shirt',
               '#add-to-cart-sauce-labs-onesie']


class OrderPage:
    """
    Этот класс создает страницу выбора и добавления товаров в корзину
    """
    def __init__(self, driver):
        """
        Функция создает страницу выбора товаров
        """
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/inventory.html')

    def do_order(self):
        """
        Эта функция позволяет добавить товары в корзину и кликнуть на
        иконку корзины для перехода на следующую страницу
        """
        with allure.step("Складываем товары в корзину"):
            for order in orders_list:
                self.driver.find_element(By.CSS_SELECTOR, order).click()

        with allure.step("Переходим на следующую страницу"):
            self.driver.find_element(By.CSS_SELECTOR,
                                     'a.shopping_cart_link').click()
