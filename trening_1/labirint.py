from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager
                                                ().install()))
driver.get('https://www.labirint.ru')

search_locator = '#search-field'
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys('Python', Keys.RETURN)

book_locator = 'div.product-card'
books = driver.find_elements(By.CSS_SELECTOR, book_locator)

for book in books:
    title = book.find_element(By.CSS_SELECTOR, 'a.product-card__name').text
    price = book.find_element(By.CSS_SELECTOR,
                              'div.product-card__price-current').text

    author = ''
    try:
        author = book.find_element(By.CSS_SELECTOR,
                                   'div.product-card__author').text
    except ValueError:
        author = "Автор не указан"

    print(author + ',' + title + ',' + price)
    sleep(1)
