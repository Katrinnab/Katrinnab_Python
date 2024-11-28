from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
sleep(3)
search_locator = '[onclick]'
for i in range(5):
    driver.find_element(By.CSS_SELECTOR, search_locator).click()

search_elements = driver.find_elements(By.XPATH, "//button[text()='Delete']")
print(f'Размер списка = {len(search_elements)}')
