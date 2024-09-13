from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from src.locators import Locators
from data import URL


class TestConstructorTabs:

    def test_buns_tab(self, driver):
        driver.get(URL.MAIN_PAGE_URL)
        wait = WebDriverWait(driver, 10)
        buns_tab = wait.until(expected_conditions.presence_of_element_located(*Locators.BUNS_TAB)).click()
        assert "current" in buns_tab.get_attribute("class")

    def test_sauces_tab(self, driver):
        driver.get(URL.MAIN_PAGE_URL)
        wait = WebDriverWait(driver, 10)
        sauces_tab = wait.until(expected_conditions.presence_of_element_located(*Locators.SAUCES_TAB)).click()
        assert "current" in sauces_tab.get_attribute("class")

    def test_fillings_tab(self, driver):
        driver.get(URL.MAIN_PAGE_URL)
        wait = WebDriverWait(driver, 10)
        fillings_tab = wait.until(expected_conditions.presence_of_element_located(*Locators.FILLINGS_TAB)).click()
        assert "current" in fillings_tab.get_attribute("class")
