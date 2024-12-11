import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_total():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    username = driver.find_element(By.CSS_SELECTOR, '#user-name')
    username.send_keys('standard_user')

    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('secret_sauce')

    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    driver.find_element(By.CSS_SELECTOR,
                        '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR,
                        '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
    first_name.send_keys('Ekaterina')
    last_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
    last_name.send_keys('Nabatova')
    postal_code = driver.find_element(By.CSS_SELECTOR, '#postal-code')
    postal_code.send_keys('198412')
    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    total = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
    driver.quit()

    assert total == 'Total: $58.29'

    driver.quit()
