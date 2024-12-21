from selenium.webdriver.common.by import By

orders_list = ['#add-to-cart-sauce-labs-backpack',
               '#add-to-cart-sauce-labs-bolt-t-shirt',
               '#add-to-cart-sauce-labs-onesie']


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/inventory.html')

    def do_order(self):
        for order in orders_list:
            self.driver.find_element(By.CSS_SELECTOR, order).click()

        self.driver.find_element(By.CSS_SELECTOR,
                                 'a.shopping_cart_link').click()
