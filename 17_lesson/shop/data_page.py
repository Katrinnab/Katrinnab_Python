from selenium.webdriver.common.by import By


class DataPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/checkout-step-one.html')

    def set_data(self):
        first_name = self.driver.find_element(By.CSS_SELECTOR, '#first-name')
        first_name.send_keys('Ekaterina')
        last_name = self.driver.find_element(By.CSS_SELECTOR, '#last-name')
        last_name.send_keys('Nabatova')
        postal_code = self.driver.find_element(By.CSS_SELECTOR, '#postal-code')
        postal_code.send_keys('198412')
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()
