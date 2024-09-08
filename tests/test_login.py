from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import LOGIN_EMAIL_FIELD, LOGIN_PASSWORD_FIELD, LOGIN_BUTTON, PERSONAL_ACCOUNT_BUTTON, \
    REGISTRATION_BUTTON, RESET_PASSWORD_BUTTON


def login(driver, email, password):
    wait = WebDriverWait(driver, 10)
    email_field = wait.until(expected_conditions.presence_of_element_located((By.XPATH, LOGIN_EMAIL_FIELD)))
    password_field = wait.until(expected_conditions.presence_of_element_located((By.XPATH, LOGIN_PASSWORD_FIELD)))
    login_button = wait.until(expected_conditions.presence_of_element_located((By.XPATH, LOGIN_BUTTON)))
    email_field.send_keys(email)
    password_field.send_keys(password)
    login_button.click()

    # Проверка успешного входа
    assert driver.current_url == "https://stellarburgers.nomoredomains.site", "Login failed"

def test_login_from_main_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoredomains.site")
    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    login(driver, "svetlanashaykhlislamova987@ya.ru", "svetlana987")
    driver.quit()

def test_login_from_personal_account_button():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoredomains.site")
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()
    login(driver, "svetlanashaykhlislamova987@ya.ru", "svetlana987")
    driver.quit()

def test_login_from_registration_form():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoredomains.site/register")
    driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()
    login(driver, "svetlanashaykhlislamova987@ya.ru", "svetlana987")
    driver.quit()

def test_login_from_reset_password_form():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoredomains.site/forgot-password")
    driver.find_element(By.XPATH, RESET_PASSWORD_BUTTON).click()
    login(driver, "svetlanashaykhlislamova987@ya.ru", "svetlana987")
    driver.quit()