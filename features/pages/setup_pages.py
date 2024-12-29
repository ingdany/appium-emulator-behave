from appium.webdriver.common.appiumby import AppiumBy
from pages.utils.base_page_object import BasePageObject


class SetupPages(BasePageObject):
    def __init__(self, driver):
        super().__init__(driver)
        # self.settings_title = (AppiumBy.XPATH, '//*[@text="Settings"]')
        self.next_button = (
            AppiumBy.XPATH,
            '//android.widget.Button[@resource-id="org.simple.clinic.staging:id/nextButton"]',
        )

    def click_next_button(self):
        self.click_element(self.next_button)
