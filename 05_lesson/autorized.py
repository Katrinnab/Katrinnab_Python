from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Firefox(options=options)

driver.get('http://the-internet.herokuapp.com/login')
search_input = driver.find_element(By.CSS_SELECTOR, '#username')
search_input.send_keys('tomsmith')
sleep(1)
search_input1 = driver.find_element(By.CSS_SELECTOR, '#password')
search_input1.send_keys('SuperSecretPassword!')
sleep(1)
search_input2 = driver.find_element(By.CSS_SELECTOR, 'button.radius')
search_input2.click()
sleep(2)

driver.quit()
