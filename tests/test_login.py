from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from data import URL
from src.helpers import generate_unique_email, generate_password
from src.locators import Locators


class TestLogin:

    def test_login_from_main_page(self, driver):
        driver.get(URL.MAIN_PAGE_URL)
        driver.find_element(Locators.LOGIN_BUTTON_MAIN).click()
        unique_email = generate_unique_email()
        unique_password = generate_password()

        wait = WebDriverWait(driver, 10)
        email_field = wait.until(expected_conditions.presence_of_element_located(Locators.LOGIN_EMAIL_FIELD))
        password_field = wait.until(expected_conditions.presence_of_element_located(Locators.LOGIN_PASSWORD_FIELD))
        login_button = wait.until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON_MAIN))
        email_field.send_keys(unique_email)
        password_field.send_keys(unique_password)
        login_button.click()

        assert driver.current_url == URL.MAIN_PAGE_URL

    def test_login_from_personal_account_button(self, driver):
        driver.get(URL.MAIN_PAGE_URL)
        driver.find_element(Locators.PERSONAL_ACCOUNT_BUTTON).click()
        unique_email = generate_unique_email()
        unique_password = generate_password()

        wait = WebDriverWait(driver, 10)
        email_field = wait.until(expected_conditions.presence_of_element_located(Locators.LOGIN_EMAIL_FIELD))
        password_field = wait.until(expected_conditions.presence_of_element_located(Locators.LOGIN_PASSWORD_FIELD))
        login_button = wait.until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON_MAIN))
        email_field.send_keys(unique_email)
        password_field.send_keys(unique_password)
        login_button.click()

        assert driver.current_url == URL.MAIN_PAGE_URL

    def test_login_from_registration_form(self, driver):
        driver.get(URL.REGISTRATION_PAGE_URL)
        driver.find_element(Locators.REGISTRATION_BUTTON_FIELD).click()
        unique_email = generate_unique_email()
        unique_password = generate_password()

        wait = WebDriverWait(driver, 10)
        email_field = wait.until(expected_conditions.presence_of_element_located(Locators.LOGIN_EMAIL_FIELD))
        password_field = wait.until(expected_conditions.presence_of_element_located(Locators.LOGIN_PASSWORD_FIELD))
        login_button = wait.until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON_MAIN))
        email_field.send_keys(unique_email)
        password_field.send_keys(unique_password)
        login_button.click()

        assert driver.current_url == URL.MAIN_PAGE_URL

    def test_login_from_reset_password_form(self, driver):
        driver.get(URL.RESET_PASSWORD_PAGE_URL)
        driver.find_element(Locators.LOGIN_BUTTON_FORGOT_PASSWORD).click()
        unique_email = generate_unique_email()
        unique_password = generate_password()

        wait = WebDriverWait(driver, 10)
        email_field = wait.until(expected_conditions.presence_of_element_located(Locators.LOGIN_EMAIL_FIELD))
        password_field = wait.until(expected_conditions.presence_of_element_located(Locators.LOGIN_PASSWORD_FIELD))
        login_button = wait.until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON_MAIN))
        email_field.send_keys(unique_email)
        password_field.send_keys(unique_password)
        login_button.click()

        assert driver.current_url == URL.MAIN_PAGE_URL
