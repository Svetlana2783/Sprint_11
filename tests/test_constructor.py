# tests/test_constructor_tabs.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import BUNS_TAB, SAUCES_TAB, FILLINGS_TAB
from data import MAIN_PAGE_URL

class TestConstructorTabs:

    def test_buns_tab(self, driver):
        driver.get(MAIN_PAGE_URL)
        wait = WebDriverWait(driver, 10)

        # Переход к разделу «Булки»
        buns_tab = wait.until(expected_conditions.presence_of_element_located((By.XPATH, BUNS_TAB)))
        buns_tab.click()
        assert "current" in buns_tab.get_attribute("class"), "Buns tab is not selected"

    def test_sauces_tab(self, driver):
        driver.get(MAIN_PAGE_URL)
        wait = WebDriverWait(driver, 10)

        # Переход к разделу «Соусы»
        sauces_tab = wait.until(expected_conditions.presence_of_element_located((By.XPATH, SAUCES_TAB)))
        sauces_tab.click()
        assert "current" in sauces_tab.get_attribute("class"), "Sauces tab is not selected"

    def test_fillings_tab(self, driver):
        driver.get(MAIN_PAGE_URL)
        wait = WebDriverWait(driver, 10)

        # Переход к разделу «Начинки»
        fillings_tab = wait.until(expected_conditions.presence_of_element_located((By.XPATH, FILLINGS_TAB)))
        fillings_tab.click()
        assert "current" in fillings_tab.get_attribute("class"), "Fillings tab is not selected"
