from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    """
    Класс создает экземпляр страницы для выполнения вычислений в калькуляторе
    """
    def __init__(self, driver, secs):
        """
        Эта функция создает страницу браузера
        """
        self.driver = driver
        self.secs = secs

    def set_delay(self):
        """
        Эта функция задает время ожидания в калькулятуре
        """
        delay = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys(self.secs)

    def set_char(self, char):
        """
        Вводим символы в окошко калькулятора
        """
        s = f"//span[text()='{char}']"
        self.driver.find_element(By.XPATH, s).click()

    def wait_for_calc(self):
        """
        Ожидаем появление результата
        """
        WebDriverWait(self.driver, self.secs).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'),
                                                 '15'))

    def get_calc(self):
        """
        Эта функция возвращает результат с экрана калькулятора
        """
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text
