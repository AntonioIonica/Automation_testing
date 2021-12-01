"""
Checkbox status
2 checkboxes
"""
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Checkboxes(BasePage):
    CHECKBOX_1 = (By.XPATH, '//*[@id="checkboxes"]/input[1]')
    CHECKBOX_2 = (By.XPATH, '//*[@id="checkboxes"]/input[2]')

    def