from selenium.webdriver.common.by import By
import allure


class CartPage:
    """
    Этот класс создает экземпляр страницы корзины
    """
    def __init__(self, driver):
        """
        Открывается страница корзины
        """
        with allure.step("Создаем страницу корзины"):
            self.driver = driver
            self.driver.get('https://www.saucedemo.com/cart.html')

    def check_orders(self):
        """
        Кликаем на кнопку Checkout для перехода на следующую страницу
        """
        with allure.step("Переход на следующую страницу"):
            self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()
