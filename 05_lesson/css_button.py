from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Возникает какой то конфликт и куча ошибок. Добавила этот блок
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

driver.get('http://uitestingplayground.com/classattr')
sleep(3)
blue_button = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '),' btn-primary ')]")
print(f'class = {blue_button.get_attribute('class')}')
blue_button.click()
