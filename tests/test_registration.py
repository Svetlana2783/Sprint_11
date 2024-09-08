from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import REGISTRATION_PAGE_URL, REGISTRATION_NAME_FIELD, REGISTRATION_EMAIL_FIELD, \
    REGISTRATION_PASSWORD_FIELD, REGISTRATION_BUTTON


def test_successful_registration():
    driver = webdriver.Chrome()
    driver.get(REGISTRATION_PAGE_URL)

    wait = WebDriverWait(driver, 10)

    name_field = wait.until(expected_conditions.presence_of_element_located((By.XPATH, REGISTRATION_NAME_FIELD)))
    email_field = wait.until(expected_conditions.presence_of_element_located((By.XPATH, REGISTRATION_EMAIL_FIELD)))
    password_field = wait.until(expected_conditions.presence_of_element_located((By.XPATH, REGISTRATION_PASSWORD_FIELD)))
    register_button = wait.until(expected_conditions.presence_of_element_located((By.XPATH, REGISTRATION_BUTTON)))

    name_field.send_keys("Светлана")
    email_field.send_keys("svetlanashaykhlislamova987@ya.ru")
    password_field.send_keys("svetlana987")
    register_button.click()

    # Проверка успешной регистрации
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Registration failed"

    driver.quit()

def test_invalid_password():
    driver = webdriver.Chrome()
    driver.get(REGISTRATION_PAGE_URL)

    wait = WebDriverWait(driver, 10)

    name_field = wait.until(expected_conditions.presence_of_element_located((By.XPATH, REGISTRATION_NAME_FIELD)))
    email_field = wait.until(expected_conditions.presence_of_element_located((By.XPATH, REGISTRATION_EMAIL_FIELD)))
    password_field = wait.until(expected_conditions.presence_of_element_located((By.XPATH, REGISTRATION_PASSWORD_FIELD)))
    register_button = wait.until(expected_conditions.presence_of_element_located((By.XPATH, REGISTRATION_BUTTON)))

    name_field.send_keys("Светлана")
    email_field.send_keys("svetlanashaykhlislamova987@ya.ru")
    password_field.send_keys("svetlana789")
    register_button.click()

    # Проверка ошибки для некорректного пароля
    error_message = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")))
    assert error_message.text == "Некорректный пароль", "Incorrect password error message not found"

    driver.quit()