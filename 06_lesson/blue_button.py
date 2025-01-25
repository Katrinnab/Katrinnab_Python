from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('http://uitestingplayground.com/ajax')
driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()
blue_button = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "content"))
    )
print(driver.find_element(By.CSS_SELECTOR, '.bg-success').text)

driver.quit()
