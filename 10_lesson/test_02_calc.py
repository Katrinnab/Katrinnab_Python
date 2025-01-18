import pytest
from selenium import webdriver
from calc_page import CalcPage
import allure


@pytest.fixture()
def driver():
    with allure.step("Настраиваем браузер для работы"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        yield driver
        driver.quit()


@allure.title("Тест вычисления суммы")
@allure.description("Вводим значения в калькулятор, ожидаем вычисления результата")
@allure.feature("Заполнение полей, ожидание суммы")
@allure.severity(allure.severity_level.NORMAL)
def test_calc(driver):
    """
    Эта функция создает страницу калькулятора и проводит вычисления
    """
    calc_page = CalcPage(driver, 45)

    with allure.step("Задаем время ожидания результата расчета"):
        calc_page.set_delay()

    with allure.step("Вводим значения для вычисления"):
        calc_page.set_char('7')
        calc_page.set_char('+')
        calc_page.set_char('8')
        calc_page.set_char('=')

    with allure.step("Ожидаем результата заданное время, проверяем условие"):
        calc_page.wait_for_calc()
    assert calc_page.get_calc() == '15'
