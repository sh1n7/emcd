from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from time import sleep


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.web_url = "https://qa-test.emcd.io/"

    def open_page(self):
        self.driver.get(self.web_url)

    def is_verify_text(self, locator, text):
        try:
            element = self.driver.find_element(*locator)
            is_verify_text = str(text) in element.text
            return is_verify_text
        except Exception as e:
            print(e)

    def wait_visibility_element(self, locator):
        try:
            self.wait.until(visibility_of_element_located((locator[0], locator[1])))
            return True
        except WebDriverException:
            return False

    def current_url(self, url):
        is_current_url = url == self.driver.current_url
        sleep(0.2)
        return is_current_url

    def input_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        sleep(0.2)
        element.send_keys(text)
        sleep(0.2)

    def click_element(self, locator):
        element = self.driver.find_element(*locator)
        element.click()
        sleep(0.2)
