from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Firefox(options=options)

driver.get('http://the-internet.herokuapp.com/entry_ad')
sleep(3)
close = driver.find_element(By.XPATH, "//p[text()='Close']").click()

driver.quit()
