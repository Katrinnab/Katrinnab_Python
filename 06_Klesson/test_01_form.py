import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_execute_form():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    my_first_name = '[name = first-name]'
    first_name = driver.find_element(By.CSS_SELECTOR, my_first_name)
    first_name.send_keys('Иван')

    my_last_name = '[name = last-name]'
    last_name = driver.find_element(By.CSS_SELECTOR, my_last_name)
    last_name.send_keys('Петров')

    my_address = '[name = address]'
    address = driver.find_element(By.CSS_SELECTOR, my_address)
    address.send_keys('Ленина, 55-3')

    my_email = '[name = e-mail]'
    email = driver.find_element(By.CSS_SELECTOR, my_email)
    email.send_keys('test@skypro.com')

    my_phone = '[name = phone]'
    phone = driver.find_element(By.CSS_SELECTOR, my_phone)
    phone.send_keys('+7985899998787')

    my_city = '[name = city]'
    city = driver.find_element(By.CSS_SELECTOR, my_city)
    city.send_keys('Москва')

    my_country = '[name = country]'
    country = driver.find_element(By.CSS_SELECTOR, my_country)
    country.send_keys('Россия')

    my_job_position = '[name = job-position]'
    job_position = driver.find_element(By.CSS_SELECTOR, my_job_position)
    job_position.send_keys('QA')

    my_company = '[name = company]'
    company = driver.find_element(By.CSS_SELECTOR, my_company)
    company.send_keys('SkyPro')

    my_zip_code = '[name = zip-code]'
    zip_code = driver.find_element(By.CSS_SELECTOR, my_zip_code)

    driver.find_element(By.XPATH,
                        "//button[@class='btn btn-outline-primary mt-3']").click()

    WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class]")))

    assert (driver.find_element(By.ID, 'first-name').get_attribute('class') ==
            'alert py-2 alert-success')
    assert (driver.find_element(By.ID, 'last-name').get_attribute('class') ==
            'alert py-2 alert-success')
    assert (driver.find_element(By.ID, 'address').get_attribute('class') ==
            'alert py-2 alert-success')
    assert (driver.find_element(By.ID, 'e-mail').get_attribute('class') ==
            'alert py-2 alert-success')
    assert (driver.find_element(By.ID, 'phone').get_attribute('class') ==
            'alert py-2 alert-success')
    assert (driver.find_element(By.ID, 'city').get_attribute('class') ==
            'alert py-2 alert-success')
    assert (driver.find_element(By.ID, 'country').get_attribute('class') ==
            'alert py-2 alert-success')
    assert (driver.find_element(By.ID, 'job-position').get_attribute('class') ==
            'alert py-2 alert-success')
    assert (driver.find_element(By.ID, 'company').get_attribute('class') ==
            'alert py-2 alert-success')
    assert (driver.find_element(By.ID, 'zip-code').get_attribute('class') ==
            'alert py-2 alert-danger')

    driver.quit()
