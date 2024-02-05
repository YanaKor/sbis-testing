import allure
import pytest
from selenium import webdriver

from base.urls import Urls
from pages.tensor_page import TensorPage
from pages.sbis_page import SbisPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    with allure.step('Chrome browser open'):
        if request.param == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--window-size=1920,1080')
            driver = webdriver.Chrome(options=chrome_options)

    with allure.step('Firefox browser is open'):
        if request.param == 'firefox':
            driver = webdriver.Firefox()
            driver.set_window_size(1920, 1080)

    with allure.step('sbis.ru page opened'):
        driver.get(Urls.BASE_URL)

    yield driver

    with allure.step('Browser is closed'):
        driver.quit()


@pytest.fixture
def tensor_page(driver):
    yield TensorPage(driver)


@pytest.fixture
def sbis_page(driver):
    yield SbisPage(driver)
