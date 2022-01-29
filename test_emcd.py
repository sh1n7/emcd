import pytest
from resources.base_ui import BaseUITest
from resources.base_page import BasePage
from resources.locators import SiteLocators as sl


@pytest.mark.emcd
class TestFactorial(BaseUITest):

    # позитивные сценарии
    @pytest.mark.parametrize('send_text, verify_result', (
            (0, 1),
            (1, 1),
            (10, 3628800),
            (169, 4.269068009004705e+304),
            (170, 7.257415615307999e+306),
            (171, 'Infinity')
    ))
    def test_pos(self, send_text, verify_result):
        wd = BasePage(self.driver)
        wd.open_page()
        wd.input_text(sl.FIELD_NUMBER, send_text)
        wd.click_element(sl.BUTTON_CALCULATE)
        wd.wait_visibility_element(sl.BUTTON_CALCULATE)
        assert wd.is_verify_text(locator=sl.STRING_RESULT, text=f'The factorial of {send_text} is: {verify_result}')

    # негативные сценарии
    @pytest.mark.parametrize('send_text, verify_result', (
            (0.1, 'Please enter an integer'),
            ('asd', 'Please enter an integer'),
            ('', 'Please enter an integer'),
            ('1+1', 'Please enter an integer')
    ))
    def test_neg(self, send_text, verify_result):
        wd = BasePage(self.driver)
        wd.open_page()
        wd.input_text(sl.FIELD_NUMBER, send_text)
        wd.click_element(sl.BUTTON_CALCULATE)
        wd.wait_visibility_element(sl.BUTTON_CALCULATE)
        assert wd.is_verify_text(locator=sl.STRING_RESULT, text=verify_result)

    # todo 500 - при вводе отрицательных чисел, необходимо обработать событие
    @pytest.mark.skip(reason="500 - при вводе отрицательных чисел, необходимо обработать событие")
    @pytest.mark.parametrize('send_text, verify_result', (
            (-1, 'inform message'),
    ))
    def test_fix(self, send_text, verify_result):
        wd = BasePage(self.driver)
        wd.open_page()
        wd.input_text(sl.FIELD_NUMBER, send_text)
        wd.click_element(sl.BUTTON_CALCULATE)
        assert wd.is_verify_text(locator=sl.STRING_RESULT, text=verify_result)
