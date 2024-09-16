from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.locators import Locators
from data import URL
from src.helpers import generate_unique_email, generate_password, generate_name


class TestSuccessfulRegistration:
    def test_successful_registration(self, driver):
        driver.get(URL.REGISTRATION_PAGE_URL)
        unique_email = generate_unique_email()
        unique_password = generate_password()
        unique_name = generate_name()
        wait = WebDriverWait(driver, 15)
        name_field = wait.until(expected_conditions.presence_of_element_located(Locators.REGISTRATION_NAME_FIELD))
        email_field = wait.until(expected_conditions.presence_of_element_located(Locators.REGISTRATION_EMAIL_FIELD))
        password_field = wait.until(expected_conditions.presence_of_element_located(Locators.REGISTRATION_PASSWORD_FIELD))
        register_button = wait.until(expected_conditions.presence_of_element_located(Locators.REGISTRATION_BUTTON_FIELD))
        name_field.send_keys(unique_name)
        email_field.send_keys(unique_email)
        password_field.send_keys(unique_password)
        register_button.click()
        assert driver.current_url == URL.LOGIN_PAGE_URL
