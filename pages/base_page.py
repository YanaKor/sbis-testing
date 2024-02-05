import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


from support.logger import log_func


class BasePage:

    log = log_func()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def element_is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator),
                               message=f'Failed to click on element{locator}')

    def find_element(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator),
                               message=f'Could not find element{locator}')

    def element(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator),
                               message=f'Could not find element {locator}')

    def wait_element_text_to_be_present(self, locator, text):
        self.wait.until(ec.text_to_be_present_in_element(locator, text),
                        message=f'{locator} element with text {text} is not displayed on the page')

    def element_is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator),
                               message=f'{locator} element not showing on page')

    @allure.step('Clicking on element')
    def click(self, locator):
        self.log.info(f'Element {locator} is clicked')
        return self.element_is_clickable(locator).click()

    @allure.step('Getting element text')
    def get_text(self, locator):
        self.log.info(f'Locator {locator} text received')
        return self.element_is_visible(locator).text

    @allure.step('Go to new tab')
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Checking that the current url contains text')
    def checking_text_in_current_url(self, text):
        self.log.info(f'The browser opened the desired page')
        return self.wait.until(ec.url_contains(text))

    @allure.step('Clicking a button in a block')
    def click_on_button_in_blocks(self, locator):
        self.log.info(f'Element {locator} is clicked')
        self.driver.find_element(locator)
        return self.driver.execexecute_script("arguments[0].click();", locator)

    @allure.step('Checking the tab title')
    def checking_browser_tab_title(self):
        self.log.info('The tab name is as expected')
        self.log.info(f'')
        return self.driver.title
