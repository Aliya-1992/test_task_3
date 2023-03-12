import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage


@pytest.fixture(scope='session')
def get_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def main_page_router(get_driver):
    return MainPage(get_driver)


@pytest.fixture(scope='session')
def registration_page_router(get_driver):
    return RegistrationPage(get_driver)


@pytest.fixture(scope='session', autouse=True)
def main_page(main_page_router):
    main_page_router.main_page()
