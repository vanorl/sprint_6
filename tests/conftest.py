import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from urls import main_site


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def order_driver(driver):
    order_page = MainPage(driver)
    order_page.accept_cookies()
    order_page.click_on_element(MainPageLocators.BODY_ORDER_BUTTON)

    return driver
