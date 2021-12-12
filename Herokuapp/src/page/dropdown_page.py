"""
DropDown checking and selecting option 1
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Herokuapp.src.page.base_page import BasePage


class DropDown(BasePage):
    DROPDOWN = (By.ID, 'dropdown')

    def click_on_option_1(self):
        element = self.driver.find_element(*self.DROPDOWN)
        drop_down = Select(element)
        drop_down.select_by_index(1)
        all_options = drop_down.options[1:]
        for option in all_options:
            print(option.text)

    def click_on_option_2(self):
        element = self.driver.find_element(*self.DROPDOWN)
        drop_down = Select(element)
        drop_down.select_by_index(2)
        all_options = drop_down.options[1:]
        for option in all_options:
            print(option.text)
