from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Firefox(options=options)

driver.get('http://the-internet.herokuapp.com/inputs')
search_input = driver.find_element(By.CSS_SELECTOR, 'input')
search_input.send_keys('1000', Keys.RETURN)
sleep(2)
search_input.clear()
search_input.send_keys('999', Keys.RETURN)
sleep(2)

driver.quit()
