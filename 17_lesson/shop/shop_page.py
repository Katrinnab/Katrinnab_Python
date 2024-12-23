from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/')

    def get_authorization(self):
        username = self.driver.find_element(By.CSS_SELECTOR, '#user-name')
        username.send_keys('standard_user')
        password = self.driver.find_element(By.CSS_SELECTOR, '#password')
        password.send_keys('secret_sauce')
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()
