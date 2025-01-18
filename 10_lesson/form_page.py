from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    """
    Этот класс создает экземпляр страницы заполнения данных и предоставляет
    методы для взаимодействия с формой
    """
    def __init__(self, driver):
        self.driver = driver

    def set_fields(self):
        """
        Эта функция заполняет поля ввода необходимыми данными
        Параметры:
            first_name (str): Имя пользователя.
            last_name (str): Фамилия пользователя.
            address (str): Адрес пользователя.
            email (str): Электронная почта пользователя.
            phone (str): Телефон пользователя.
            city (str): Город пользователя.
            country (str): Страна пользователя.
            job_position (str): Должность пользователя.
            company (str): Компания пользователя.
        """

        my_first_name = '[name = first-name]'
        first_name = self.driver.find_element(By.CSS_SELECTOR, my_first_name)
        first_name.send_keys('Иван')

        my_last_name = '[name = last-name]'
        last_name = self.driver.find_element(By.CSS_SELECTOR, my_last_name)
        last_name.send_keys('Петров')

        my_address = '[name = address]'
        address = self.driver.find_element(By.CSS_SELECTOR, my_address)
        address.send_keys('Ленина, 55-3')

        my_email = '[name = e-mail]'
        email = self.driver.find_element(By.CSS_SELECTOR, my_email)
        email.send_keys('test@skypro.com')

        my_phone = '[name = phone]'
        phone = self.driver.find_element(By.CSS_SELECTOR, my_phone)
        phone.send_keys('+7985899998787')

        my_city = '[name = city]'
        city = self.driver.find_element(By.CSS_SELECTOR, my_city)
        city.send_keys('Москва')

        my_country = '[name = country]'
        country = self.driver.find_element(By.CSS_SELECTOR, my_country)
        country.send_keys('Россия')

        my_job_position = '[name = job-position]'
        job_position = self.driver.find_element(By.CSS_SELECTOR,
                                                my_job_position)
        job_position.send_keys('QA')

        my_company = '[name = company]'
        company = self.driver.find_element(By.CSS_SELECTOR, my_company)
        company.send_keys('SkyPro')

        my_zip_code = '[name = zip-code]'
        zip_code = self.driver.find_element(By.CSS_SELECTOR, my_zip_code)
        zip_code.send_keys('')

    def click_submit(self):
        """
        Эта функция отправляет заполненную форму по клику на кнопку Submit
        после окончания ввода данных
        """
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def wait_all_fields(self):
        """
        Ожидаем заполнения и появления всех элементов
        """
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                 "div[class]")))

    def field_status(self, key):
        """
        Эта функция возвращает значения параметров в необходимые поля
        """
        return self.driver.find_element(By.ID, key).get_attribute('class')
