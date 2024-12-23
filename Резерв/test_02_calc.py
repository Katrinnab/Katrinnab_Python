import pytest
from selenium import webdriver
from calc_page import CalcPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calc(driver):
    calc_page = CalcPage(driver, 45)
    calc_page.set_delay()
    calc_page.set_char('7')
    calc_page.set_char('+')
    calc_page.set_char('8')
    calc_page.set_char('=')
    calc_page.wait_for_calc()
    assert calc_page.get_calc() == '15'
