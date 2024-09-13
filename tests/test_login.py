from src.locators import Locators
from data import URL
from helpers import generate_unique_email, generate_password, login

class TestLogin:

    def test_login_from_main_page(self, driver):
        driver.get(URL.MAIN_PAGE_URL)
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        unique_email = generate_unique_email()
        unique_password = generate_password()
        login(driver, unique_email, unique_password)
        assert driver.current_url == URL.MAIN_PAGE_URL, "Login failed"

    def test_login_from_personal_account_button(self, driver):
        driver.get(URL.MAIN_PAGE_URL)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        unique_email = generate_unique_email()
        unique_password = generate_password()
        login(driver, unique_email, unique_password)
        assert driver.current_url == URL.MAIN_PAGE_URL, "Login failed"

    def test_login_from_registration_form(self, driver):
        driver.get(URL.REGISTRATION_PAGE_URL)
        driver.find_element(*Locators.REGISTRATION_BUTTON_FIELD).click()
        unique_email = generate_unique_email()
        unique_password = generate_password()
        login(driver, unique_email, unique_password)
        assert driver.current_url == URL.MAIN_PAGE_URL

    def test_login_from_reset_password_form(self, driver):
        driver.get(URL.RESET_PASSWORD_PAGE_URL)
        driver.find_element(*Locators.LOGIN_BUTTON_FORGOT_PASSWORD).click()
        unique_email = generate_unique_email()
        unique_password = generate_password()
        login(driver, unique_email, unique_password)
        assert driver.current_url == URL.MAIN_PAGE_URL