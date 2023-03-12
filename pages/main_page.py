import time
from random import uniform
from base_class.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class MainPage(Base):
    def __init__(self, driver, url='https://piter-online.net/'):
        super().__init__(driver, url)

    # Locators
    field_for_address = '(//input[@datatest="main_input_street_home_new"])[1]'  # поле ввода 'введите улицу'
    address = 'Тестовая линия'
    address_from_list = '//*[@class="app141 app150 app148 app147 app143 app160 app142"]'  # название улицы из выпадающего списка
    field_for_number_of_house = '(//input[@datatest="main_input_street_home_new"])[2]'  # поле ввода "дом"
    type_of_connection = '(//span[@class="app177 app178 icon24 icon-arrow-1-down"])[1]'  # раскрывающийся список 'тип подключения'
    point_in_flat = '(//li[text()="В квартиру"])[1]'  # Пункт "В квартире"
    button_to_show_rate = '(//div[@data-test="find_tohome_button"])[1]'  # кнопка "показать тарифы"
    button_for_close = '//div[@datatest="close_popup1_from_quiz_input_tel"]'  # кнопка для закрытия всплывающего окно

    # Getters
    def get_field_for_address(self):
        """
        Этот метод возвращает поле для ввода адреса
        """

        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.field_for_address)))

    def get_address_from_list(self):
        """
        Этот метод возвращает адрес из выпадающего списка
        """

        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.address_from_list)))

    def get_field_for_number_of_house(self):
        """
        Этот метод возвращает поле для ввода номера дома
        """

        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.field_for_number_of_house)))

    def get_type_of_connection(self):
        """
        Этот метод возвращает раскрывающийся список 'Тип подключения'
        """

        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.type_of_connection)))

    def get_point_in_flat(self):
        """
        Этот метод возвращает пункт в списке 'В квартире'
        """

        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.point_in_flat)))

    def get_button_to_show_rate(self):
        """
        Этот метод возвращает кнопку 'Показать тарифы'
        """

        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_to_show_rate)))

    def get_button_for_close(self):
        """
        Этот метод возвращает кнопку для закрытия всплывающего окна
        """

        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_for_close)))

    # Actions
    def input_address(self):
        """
        Этот метод позволяет указать улицу
        """

        self.action.double_click(self.get_field_for_address()).perform()
        self.get_field_for_address().send_keys(self.address)
        time.sleep(uniform(0, 1))
        self.get_field_for_address().send_keys(Keys.ENTER)

    def input_number_of_house(self):
        """
        Этот метод позволяет указать номер дома
        """

        time.sleep(uniform(1, 2))
        self.action.double_click(self.get_field_for_number_of_house()).perform()
        self.get_field_for_number_of_house().send_keys('1')

    def click_type_of_connection(self):
        """
        Этот метод позволяет нажать на раскрывающийся список
        """

        self.action.move_to_element(self.get_type_of_connection()).click().perform()

    def click_point_in_flat(self):
        """
        Этот метод позволяет выбрать пункт "В квартире
        """

        self.action.move_to_element(self.get_point_in_flat()).click().perform()

    def click_button_to_show_rate(self):
        """
        Этот метод позволяет нажать на кнопку "Показать тарифы
        """

        self.action.double_click(self.get_button_to_show_rate()).perform()

    def click_button_for_close(self):
        """
        Этот метод позволяет закрыть всплывающее окно
        """

        time.sleep(uniform(2, 3))
        self.action.move_to_element(self.get_button_for_close()).click().perform()

    def main_page(self):
        """
        Этот метод позволяет заполнить адрес для составления заявки
        """

        self.get_current_url()
        self.input_address()
        self.input_number_of_house()
        self.click_type_of_connection()
        self.click_point_in_flat()
        self.click_button_to_show_rate()
        self.click_button_for_close()
