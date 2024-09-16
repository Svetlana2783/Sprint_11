from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.locators import Locators
from data import URL

class TestNavigation:

    def test_navigate_to_personal_account(self, driver):
        driver.get(URL.MAIN_PAGE_URL)
        wait = WebDriverWait(driver, 15)
        wait.until(expected_conditions.presence_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        assert driver.current_url == URL.PROFILE_PAGE_URL

    def test_navigate_to_constructor_from_personal_account(self, driver):
        driver.get(URL.PROFILE_PAGE_URL)
        wait = WebDriverWait(driver, 15)
        wait.until(expected_conditions.presence_of_element_located(Locators.CONSTRUCTOR_BUTTON)).click()
        assert driver.current_url == URL.MAIN_PAGE_URL

    def test_navigate_to_constructor_via_logo(self, driver):
        driver.get(URL.PROFILE_PAGE_URL)
        wait = WebDriverWait(driver, 15)
        wait.until(expected_conditions.presence_of_element_located(Locators.LOGO)).click()
        assert driver.current_url == URL.MAIN_PAGE_URL