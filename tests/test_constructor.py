from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import BUNS_TAB, SAUCES_TAB, FILLINGS_TAB

def test_constructor_tabs():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    wait = WebDriverWait(driver, 10)

    # Переход к разделу «Булки»
    buns_tab = wait.until(expected_conditions.presence_of_element_located((By.XPATH, BUNS_TAB)))
    buns_tab.click()
    assert buns_tab.is_selected(), "Buns tab is not selected"

    # Переход к разделу «Соусы»
    sauces_tab = wait.until(expected_conditions.presence_of_element_located((By.XPATH, SAUCES_TAB)))
    sauces_tab.click()
    assert sauces_tab.is_selected(), "Sauces tab is not selected"

    # Переход к разделу «Начинки»
    fillings_tab = wait.until(expected_conditions.presence_of_element_located((By.XPATH, FILLINGS_TAB)))
    fillings_tab.click()
    assert fillings_tab.is_selected(), "Fillings tab is not selected"

    driver.quit()