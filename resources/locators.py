from selenium.webdriver.common.by import By


class SiteLocators(object):

    FIELD_NUMBER = (By.ID, "number")
    BUTTON_CALCULATE = (By.ID, "getFactorial")
    STRING_RESULT = (By.ID, "resultDiv")
