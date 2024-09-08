import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import LOGOUT_BUTTON

def test_logout():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/account/profile")

    wait = WebDriverWait(driver, 10)

    wait.until(expected_conditions.presence_of_element_located((By.XPATH, LOGOUT_BUTTON))).click()

    # Проверка выхода из аккаунта
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Logout failed"

    driver.quit()