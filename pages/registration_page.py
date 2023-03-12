import time
import requests
from random import uniform
from base_class.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RegistrationPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #Locators
    button_for_connection = '//a[@href="/leningradskaya-oblast/orders/home?tariff_id=102134004"]'
    field_for_name = '//*[@datatest="providers_provider_order_input_name"]'
    name = 'Автотест'
    field_for_number = '//*[@datatest="providers_provider_order_input_tel"]'
    number = '1111111111'
    button_to_leave_application = '//*[@data-test="order_form_input_connect_button"]'

    # Getters
    def get_button_for_connection(self):
        """
        Этот метод возвращает кнопку 'Показать тарифы'
        """

        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_for_connection)))

    def get_field_for_name(self):
        """
        Этот метод возвращает поле ввода 'Имя'
        """

        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.field_for_name)))

    def get_field_for_number(self):
        """
        Этот метод возвращает поле ввода 'Мобильный телефон'
        """

        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.field_for_number)))

    def get_button_to_leave_application(self):
        """
        Этот метод возвращает кнопку 'оставить заявку'
        """

        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_to_leave_application)))

    def get_status_code(self):
        url = self.driver.current_url
        result = requests.get(url)
        return result.status_code

    #Actions
    def click_button_for_connection(self):
        time.sleep(uniform(0, 1))
        self.action.move_to_element(self.get_button_for_connection()).click().perform()

    def input_name(self):
        """
        Этот метод позволяет указать номер дома
        """

        self.action.double_click(self.get_field_for_name()).perform()
        self.get_field_for_name().send_keys(self.name)

    def input_number(self):
        """
        Этот метод позволяет указать номер дома
        """

        self.action.double_click(self.get_field_for_number()).perform()
        self.get_field_for_number().send_keys(self.number)

    def click_button_to_leave_application(self):
        """
        Этот метод позволяет нажать на кнопку "Оставить заявку"
        """

        time.sleep(uniform(0, 1))
        self.action.double_click(self.get_button_to_leave_application()).perform()

    def registration_page(self):
        """
        Этот метод позволяет зарегистрировать заявку
        """

        self.click_button_for_connection()
        self.input_name()
        self.input_number()
        self.click_button_to_leave_application()
        time.sleep(uniform(0, 1))
