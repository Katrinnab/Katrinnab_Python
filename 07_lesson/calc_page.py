from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver, secs):
        self.driver = driver
        self.secs = secs

    def set_delay(self):
        delay = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys(self.secs)

    def set_char(self, char):
        s = f"//span[text()='{char}']"
        self.driver.find_element(By.XPATH, s).click()

    def wait_for_calc(self):
        WebDriverWait(self.driver, self.secs).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15'))

    def get_calc(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text
