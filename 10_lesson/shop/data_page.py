from selenium.webdriver.common.by import By
import allure


class DataPage:
    """
    Этот класс создает страницу заполнения личных данных пользователя.
    """
    def __init__(self, driver):
        """
        Создается страница заполнения личный данных после покупки
        """
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/checkout-step-one.html')

    def set_data(self):
        """
        Эта функция заполняет поля ввода личный данных клиента
        и позволяет перейти на следующую страницу
        Параметры:
                first_name (str): Имя пользователя.
                last_name (str): Фамилия пользователя.
                postal_code (str): Почтовый индекс.
        """
        with allure.step("Заполняем поля ввода информации о клиенте"):
            first_name = self.driver.find_element(By.CSS_SELECTOR, '#first-name')
            first_name.send_keys('Ekaterina')
            last_name = self.driver.find_element(By.CSS_SELECTOR, '#last-name')
            last_name.send_keys('Nabatova')
            postal_code = self.driver.find_element(By.CSS_SELECTOR, '#postal-code')
            postal_code.send_keys('198412')

        with allure.step("Переходим на следующую страницу"):
            self.driver.find_element(By.CSS_SELECTOR, '#continue').click()
