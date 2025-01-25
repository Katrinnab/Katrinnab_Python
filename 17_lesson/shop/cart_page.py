from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/cart.html')

    def check_orders(self):
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()
