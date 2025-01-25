from selenium.webdriver.common.by import By
import allure


class ResultPage:
    """
    Этот класс создает конечную, результирующую страницу браузера
    с итоговой суммой заказа
    """
    def __init__(self, driver):
        """
        Открываем итоговоую страницу заказа
        """
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/checkout-step-two.html')

    def get_total(self):
        """
        Эта функция возвращает сумму заказа
        """
        with allure.step("Возвращаем итоговую сумму заказа"):
            return self.driver.find_element(By.CSS_SELECTOR,
                                            'div.summary_total_label').text
