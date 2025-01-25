from selenium.webdriver.common.by import By
import allure


class ShopPage:
    """
    Этот класс создает экземпляр первой страницы сайта,
    пользователь авторизуется.
    """
    def __init__(self, driver):
        """
        Функция создает браузер и открывает страницу авторизации
        """
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/')

    def get_authorization(self):
        """
        Эта функция авторизовывает пользователя на сайте
        """
        with allure.step("Вводим данные для авторизации"):
            username = self.driver.find_element(By.CSS_SELECTOR, '#user-name')
            username.send_keys('standard_user')
            password = self.driver.find_element(By.CSS_SELECTOR, '#password')
            password.send_keys('secret_sauce')

        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()
