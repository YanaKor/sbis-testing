import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from base.urls import Urls
from support.logger import log_func


class TensorPageLocators:
    TENSOR_BANNER = (By.XPATH, ".//div[contains(@class, 'sbisru-Contacts')]//a[contains(@title, 'tensor.ru')]")
    POWER_BLOCK = (By.XPATH, ".//div[@class='tensor_ru-Index__block4-content tensor_ru-Index__card']")
    WORKING_BLOCK = (By.XPATH, ".//div[@class='tensor_ru-container tensor_ru-section tensor_ru-About__block3']")


class TensorPage(BasePage):

    log = log_func()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Clicking on the tensor banner')
    def click_on_tensor_banner(self):
        self.click(TensorPageLocators.TENSOR_BANNER)

    @allure.step('Checking the transition to the tensor.ru page')
    def check_switch_to_tensor_page(self):
        self.switch_to_new_tab()
        return self.checking_text_in_current_url(f'{Urls.TENSOR_LINK}')

    @allure.step('Checking the presence of the "Strength in People" block')
    def check_humans_power_block(self):
        self.wait_element_text_to_be_present(TensorPageLocators.POWER_BLOCK, 'Сила в людях')

    @allure.step('Go to "More details" in the "Strength in people" block')
    def click_on_more_details(self):
        details = self.find_element(TensorPageLocators.POWER_BLOCK).find_element(
            by=By.CSS_SELECTOR, value="a")
        return self.driver.execute_script("arguments[0].click();", details)

    @allure.step('Checking that the details page opens')
    def check_switch_to_more_details_page(self):
        return self.checking_text_in_current_url(f'{Urls.ABOUT_TENSOR_LINK}')

    @allure.step('Find the section "We work"')
    def find_images_in_working_block(self):
        return self.find_element(TensorPageLocators.WORKING_BLOCK).find_elements(
            by=By.CLASS_NAME, value='tensor_ru-About__block3-image')
