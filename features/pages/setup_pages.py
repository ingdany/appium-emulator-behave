from appium.webdriver.common.appiumby import AppiumBy
from pages.utils.base_page_object import BasePageObject


class SetupPages(BasePageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.next_button = (
            AppiumBy.XPATH,
            '//android.widget.Button[@resource-id="org.simple.clinic.staging:id/nextButton"]',
        )
        self.get_started_button = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("org.simple.clinic.staging:id/getStartedButton")',
        )
        self.agree_and_continue_button = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("AGREE AND CONTINUE")',
        )        
        self.country_locator_template = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("{}")',
        )
        self.city_locator_template = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("{}")',
        )
        self.phone_number_locator = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("org.simple.clinic.staging:id/phoneNumberEditText")',
        )
        self.phone_next_button = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("org.simple.clinic.staging:id/nextButton")',
        )
        self.role_full_name_locator = (
            AppiumBy.ID,
            "org.simple.clinic.staging:id/fullNameEditText",
        )
        self.role_full_name_next_button = (
            AppiumBy.ID,
            "org.simple.clinic.staging:id/nextButton",
        )
        self.pin_locator = (
            AppiumBy.ID,
            "org.simple.clinic.staging:id/pinEditText",
        )
        self.skip_button = (
            AppiumBy.ID,
            "org.simple.clinic.staging:id/skipButton",
        )
        self.facility_locator_template = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("{}")',
        )
        self.yes_button = (
            AppiumBy.ID,
            "org.simple.clinic.staging:id/yesButton",
        )
        self.skip2_button = (
            AppiumBy.ID,
            "org.simple.clinic.staging:id/skipButton",
        )
        self.allow_button = (
            AppiumBy.ID,
            "com.android.permissioncontroller:id/permission_allow_button",
        )
        self.notification_locator = (
            AppiumBy.ID,
            "com.android.permissioncontroller:id/permission_message",
        )
        self.search_patient_locator = (
            AppiumBy.ID,
            "org.simple.clinic.staging:id/searchPatientsButton",
        )

    def click_next_button(self):
        self.click_element(self.next_button)

    def click_get_started_button(self):
        self.click_element(self.get_started_button)

    def click_agree_and_continue_button(self):
        self.click_element(self.agree_and_continue_button)

    def get_country_locator(self, country):
        return (
            self.country_locator_template[0],
            self.country_locator_template[1].format(country),
        )

    def select_country(self, country):
        country_locator = self.get_country_locator(country)
        self.click_element(country_locator)

    def get_city_locator(self, city):
        return (
            self.city_locator_template[0],
            self.city_locator_template[1].format(city),
        )

    def select_city(self, city):
        city_locator = self.get_city_locator(city)
        self.click_element(city_locator)

    def set_phone_number(self, phone):      
        self.type_text(self.phone_number_locator, phone)
        self.click_element(self.phone_next_button)

    def set_role_full_name(self, role_full_name):
        self.type_text(self.role_full_name_locator, role_full_name)
        self.click_element(self.role_full_name_next_button)

    def set_pin(self, pin):
        self.type_text(self.pin_locator, pin)

    def click_skip_button(self):
        self.click_element(self.skip_button)

    def get_facility_locator(self, facility):
        return (
            self.facility_locator_template[0],
            self.facility_locator_template[1].format(facility),
        )

    def select_facility(self, facility):    
        facility_locator = self.get_facility_locator(facility)
        self.click_element(facility_locator)
        self.click_element(self.yes_button)

    def click_skip2_button(self):
        self.click_element(self.skip2_button)

    def click_allow_button(self):
        self.click_element(self.allow_button)

    def get_notification(self):
        self.find_element(self.notification_locator).is_displayed()
    
    def is_there_search_patient_button(self):
        return self.find_element(self.search_patient_locator).is_displayed()
