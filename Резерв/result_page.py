from selenium.webdriver.common.by import By


class ResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/checkout-step-two.html')

    def get_total(self):
        return self.driver.find_element(By.CSS_SELECTOR,
                                        'div.summary_total_label').text
