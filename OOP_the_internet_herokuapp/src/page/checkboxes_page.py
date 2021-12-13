"""
Checkbox status
2 checkboxes
"""
from selenium.webdriver.common.by import By

from OOP_the_internet_herokuapp.src.page.base_page import BasePage


class Checkboxes(BasePage):
    CHECKBOX_1 = (By.XPATH, '//*[@id="checkboxes"]/input[1]')
    CHECKBOX_2 = (By.XPATH, '//*[@id="checkboxes"]/input[2]')

    def double_click(self):
        box1 = self.driver.find_element(*self.CHECKBOX_1)
        box1.click()
        box1.click()

    def uncheck_box2(self):
        box2 = self.driver.find_element(*self.CHECKBOX_2)
        box2.click()
