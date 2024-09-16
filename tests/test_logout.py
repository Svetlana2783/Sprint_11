from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.locators import Locators
from data import URL


class TestLogout:

    @staticmethod
    def test_logout(driver):
        driver.get(URL.PROFILE_PAGE_URL)
        wait = WebDriverWait(driver, 15)
        wait.until(expected_conditions.presence_of_element_located(Locators.LOGOUT_BUTTON)).click()
        assert driver.current_url == URL.LOGIN_PAGE_URL
