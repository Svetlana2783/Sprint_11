from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import LOGOUT_BUTTON
from data import PROFILE_PAGE_URL, LOGIN_PAGE_URL

def test_logout(driver):
    driver.get(PROFILE_PAGE_URL)

    wait = WebDriverWait(driver, 10)

    wait.until(expected_conditions.presence_of_element_located((By.XPATH, LOGOUT_BUTTON))).click()

    # Проверка выхода из аккаунта
    assert driver.current_url == LOGIN_PAGE_URL, "Logout failed"
