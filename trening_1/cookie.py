from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()

my_cookie = {
    'name': 'cookie_policy',
    'value': '1'
}

driver.get('http://labirint.ru')
driver.add_cookie(my_cookie)

cookie = driver.get_cookie('PHPSESSID')
print(cookie)

# cookies = driver.get_cookies()
# print(cookies)

# driver.refresh()
# driver.delete_all_cookies()
# driver.refresh()

# sleep(10)
driver.quit()
