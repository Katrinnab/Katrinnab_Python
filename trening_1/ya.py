from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def make_skreenshot(browser):
    browser.maximize_window()
    browser.get('https://ya.ru')
    sleep(5)

    browser.save_screenshot('./ya_'+browser.name+'.png')
    browser.quit()


ff = webdriver.Firefox()
chrome = webdriver.Chrome()

make_skreenshot(ff)
make_skreenshot(chrome)
