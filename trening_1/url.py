from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('http://ya.ru')

url = driver.current_url

print(url)

driver.quit()
