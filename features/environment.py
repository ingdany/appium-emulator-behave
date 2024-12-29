from appium import webdriver
from appium.options.android import UiAutomator2Options
import logging
from urllib3.exceptions import MaxRetryError
from appium.webdriver.appium_connection import AppiumConnection
from appium.webdriver.appium_service import AppiumService
from features.pages.setup_pages import SetupPages


def before_scenario(context, scenario):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "uiautomator2"
    options.device_name = "sdk_gphone64_x86_64"
    options.app_package = "org.simple.clinic.staging"
    options.app_activity = "org.simple.clinic.setup.SetupActivity"
    options.language = "en"
    options.locale = "US"

    context.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    context.setup_pages = SetupPages(context.driver)


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
