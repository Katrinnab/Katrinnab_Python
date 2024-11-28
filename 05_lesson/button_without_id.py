from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Возникает какой то конфликт и куча ошибок. Добавила этот блок
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

for i in range(3):
    driver.get('http://uitestingplayground.com/dynamicid')
    sleep(3)
    value = "//button[text()='Button with Dynamic ID']"
    # blue_button = driver.find_element(By.XPATH, value).click()- по дз.
    blue_button = driver.find_element(By.XPATH, value)
    # убедимся, что кнопка нажалась 3 раза и id поменялся
    print(f'id = {blue_button.get_attribute('id')}')
