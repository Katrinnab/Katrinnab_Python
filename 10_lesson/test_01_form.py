import pytest
from selenium import webdriver
from form_page import FormPage
import allure


data_fields = {'first name': 'Иван', 'last name': 'Петров',
               'address': 'Ленина, 55-3', 'email': 'test@skypro.com',
               'Phone number': '+7985899998787', 'City': 'Москва',
               'Country': 'Россия', 'Job position': 'QA',
               'Company': 'SkyPro', 'zip-code': ''}

fields_for_test = [key for key in data_fields.keys()]
success_status = 'alert py-2 alert-success'
alert_status = 'alert py-2 alert-danger'


@pytest.fixture()
def driver():
    with allure.step("Настраиваем вебдрайвер"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        yield driver
        driver.quit()


@pytest.fixture()
def mypage(driver):
    """
    Тестирование отправки формы и валидации ее полей.
    """
    page = FormPage(driver)

    with allure.step("Заполняем поля ввода формы данными"):
        page.set_fields()

    with allure.step("Отправляем заполненную форму"):
        page.click_submit()

    with allure.step("Ожидаем появления всех элементов"):
        page.wait_all_fields()
        return page


@allure.title("Тест сравнения результатов заполнения формы")
@allure.description("Сравниваем результат заполнения полей")
@allure.feature("Проверяем все поля на соответствие статусам")
@allure.severity(allure.severity_level.NORMAL)
def test_alert_status(mypage):
    with allure.step("Валидация полей"):
        assert mypage.field_status('zip-code') == alert_status
        assert mypage.field_status('first-name') == success_status
        assert mypage.field_status('last-name') == success_status
        assert mypage.field_status('address') == success_status
        assert mypage.field_status('e-mail') == success_status
        assert mypage.field_status('phone') == success_status
        assert mypage.field_status('city') == success_status
        assert mypage.field_status('country') == success_status
        assert mypage.field_status('job-position') == success_status
        assert mypage.field_status('company') == success_status
