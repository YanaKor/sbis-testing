import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from base.urls import Urls
from support.logger import log_func


class SbisPageLocators:
    CONTACTS = (By.XPATH, ".//a[contains(@class, 'sbisru-Header') and @href='/contacts']")
    HOME_REGION = (By.XPATH,
                   ".//span[@class='sbis_ru-Region-Chooser ml-16 ml-xm-0']"
                   "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    PARTNERS_LIST = (By.XPATH, ".//div[@class='ws-flexbox sbisru-Contacts-City__flex sbisru-Contacts-Shot']")
    KAMCHATKA_KRAI_LOCATOR = (By.XPATH, "//span[contains(text(),'41 Камчатский край')]")


class SbisPage(BasePage):

    log = log_func()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Go to the "Contacts" section')
    def click_on_contacts_btn(self):
        self.click(SbisPageLocators.CONTACTS)

    @allure.step('Checking the region definition on a page')
    def checking_region_display(self):
        return self.get_text(SbisPageLocators.HOME_REGION)

    @allure.step('Checking the list of partners')
    def checking_partners_list(self):
        return self.element_is_visible(SbisPageLocators.PARTNERS_LIST)

    @allure.step('Opening a modal window for selecting regions')
    def open_region_chooser(self):
        region = self.find_element(SbisPageLocators.HOME_REGION)
        return self.driver.execute_script("arguments[0].click();", region)

    @allure.step('Change of region to Kamchatka Krai')
    def choose_kamchatka_krai(self):
        return self.click(SbisPageLocators.KAMCHATKA_KRAI_LOCATOR)

    @allure.step('Checking that the link contains information for the selected region')
    def check_switch_to_kamchatka_krai_page(self):
        return self.checking_text_in_current_url(f'{Urls.KAMCHATKA_KRAI}')



