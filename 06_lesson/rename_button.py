from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/textinput')
waiter = WebDriverWait(driver, 20)
search_input = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
my_text = 'SkyPro'
search_input.send_keys(my_text)
search_button = driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()
blue_button = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH,
                                          "//button[text()='" + my_text + "']"))
    )
print(blue_button.text)
driver.quit()
