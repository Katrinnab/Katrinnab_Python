from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys('Selenium')

search_input.send_keys(Keys.RETURN)

sleep(3)
