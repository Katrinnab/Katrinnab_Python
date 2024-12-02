from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://ya.ru')

current_title = driver.title

print(current_title)

driver.quit()
