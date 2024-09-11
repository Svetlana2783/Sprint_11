# tests/test_login.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import LOGIN_EMAIL_FIELD, LOGIN_PASSWORD_FIELD, LOGIN_BUTTON, PERSONAL_ACCOUNT_BUTTON, REGISTRATION_BUTTON, RESET_PASSWORD_BUTTON
from data import MAIN_PAGE_URL, REGISTRATION_PAGE_URL, RESET_PASSWORD_PAGE_URL
from helpers import generate_unique_email, generate_password

def login(driver, email, password):
    wait = WebDriverWait(driver, 10)
    email_field = wait.until(expected_conditions.presence_of_element_located((By.XPATH, LOGIN_EMAIL_FIELD)))
    password_field = wait.until(expected_conditions.presence_of_element_located((By.XPATH, LOGIN_PASSWORD_FIELD)))
    login_button = wait.until(expected_conditions.presence_of_element_located((By.XPATH, LOGIN_BUTTON)))
    email_field.send_keys(email)
    password_field.send_keys(password)
    login_button.click()

def test_login_from_main_page(driver):
    driver.get(MAIN_PAGE_URL)
    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    unique_email = generate_unique_email()
    unique_password = generate_password()
    login(driver, unique_email, unique_password)
    assert driver.current_url == MAIN_PAGE_URL, "Login failed"

def test_login_from_personal_account_button(driver):
    driver.get(MAIN_PAGE_URL)
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()
    unique_email = generate_unique_email()
    unique_password = generate_password()
    login(driver, unique_email, unique_password)
    assert driver.current_url == MAIN_PAGE_URL, "Login failed"

def test_login_from_registration_form(driver):
    driver.get(REGISTRATION_PAGE_URL)
    driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()
    unique_email = generate_unique_email()
    unique_password = generate_password()
    login(driver, unique_email, unique_password)
    assert driver.current_url == MAIN_PAGE_URL, "Login failed"

def test_login_from_reset_password_form(driver):
    driver.get(RESET_PASSWORD_PAGE_URL)
    driver.find_element(By.XPATH, RESET_PASSWORD_BUTTON).click()
    unique_email = generate_unique_email()
    unique_password = generate_password()
    login(driver, unique_email, unique_password)
    assert driver.current_url == MAIN_PAGE_URL, "Login failed"
