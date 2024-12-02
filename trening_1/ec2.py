from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('http://uitestingplayground.com/')

check_img = driver.find_element(By.CSS_SELECTOR, '.img-fluid')

print("Элемент 'Кубик' найден и кликнут")

driver.quit()
