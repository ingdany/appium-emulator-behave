import pytest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageObject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def type_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()
