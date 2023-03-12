from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class Base:

    def __init__(self, driver, url='https://piter-online.net/'):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 40)
        self.url = url
        self.action = ActionChains(self.driver)

    def get_current_url(self):
        """
        Этот метод позволяет открыть ссылку
        """

        self.driver.get(self.url)
        self.driver.maximize_window()

