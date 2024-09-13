import random
import string
from faker import Faker
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from src.locators import Locators

def generate_unique_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"test+{random_string}@example.com"

def generate_password():
    fake = Faker()
    return fake.password()

def generate_name():
    fake = Faker()
    return fake.name()

def login(driver, email, password):
    wait = WebDriverWait(driver, 10)
    email_field = wait.until(expected_conditions.presence_of_element_located(*Locators.LOGIN_EMAIL_FIELD))
    password_field = wait.until(expected_conditions.presence_of_element_located(*Locators.LOGIN_PASSWORD_FIELD))
    login_button = wait.until(expected_conditions.presence_of_element_located(*Locators.LOGIN_BUTTON))
    email_field.send_keys(email)
    password_field.send_keys(password)
    login_button.click()