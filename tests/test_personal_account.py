from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import PERSONAL_ACCOUNT_BUTTON, CONSTRUCTOR_BUTTON, LOGO_BUTTON

def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    wait = WebDriverWait(driver, 10)
    # Переход в личный кабинет
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, PERSONAL_ACCOUNT_BUTTON))).click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile", "Failed to navigate to personal account"

    # Переход из личного кабинета в конструктор по клику на «Конструктор»
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, CONSTRUCTOR_BUTTON))).click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Failed to navigate to constructor via constructor button"

    # Переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
    driver.get("https://stellarburgers.nomoreparties.site/account/profile")
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, LOGO_BUTTON))).click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Failed to navigate to constructor via logo button"
    driver.quit()