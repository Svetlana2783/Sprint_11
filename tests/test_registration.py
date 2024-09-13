from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from src.locators import Locators
from data import URL
from helpers import generate_unique_email, generate_password, generate_name

def register(driver, name, email, password):
    wait = WebDriverWait(driver, 10)
    name_field = wait.until(expected_conditions.presence_of_element_located(*Locators.REGISTRATION_NAME_FIELD))
    email_field = wait.until(expected_conditions.presence_of_element_located(*Locators.REGISTRATION_EMAIL_FIELD))
    password_field = wait.until(expected_conditions.presence_of_element_located(*Locators.REGISTRATION_PASSWORD_FIELD))
    register_button = wait.until(expected_conditions.presence_of_element_located(*Locators.REGISTRATION_BUTTON_FIELD))
    name_field.send_keys(name)
    email_field.send_keys(email)
    password_field.send_keys(password)
    register_button.click()

class TestRegistration:
    def test_successful_registration(driver):
        driver.get(URL.REGISTRATION_PAGE_URL)
        unique_email = generate_unique_email()
        unique_password = generate_password()
        unique_name = generate_name()
        register(driver, unique_name, unique_email, unique_password)
        assert driver.current_url == URL.LOGIN_PAGE_URL

    def test_invalid_password(driver):
        driver.get(URL.REGISTRATION_PAGE_URL)
        unique_email = generate_unique_email()
        unique_name = generate_name()
        register(driver, unique_name, unique_email, "invalid")
        wait = WebDriverWait(driver, 10)
        error_message = wait.until(expected_conditions.presence_of_element_located(*Locators.PASS_ERROR_LABEL))
        assert error_message.text == "Некорректный пароль"
