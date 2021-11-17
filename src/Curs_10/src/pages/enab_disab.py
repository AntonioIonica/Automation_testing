"""
Enabled and disabled elements
checking using is_enabled()
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class EnabledDisabledEle(BasePage):
    ENABLED_ELE = (By.ID, 'input')
    DISABLED_ELE = (By.ID, 'disabledInput')

    def disabled_check(self):
        enabled_check = self.driver.find_element(*self.ENABLED_ELE)
        status_enabled = enabled_check.is_enabled()
        print(f'Enabled box status is {status_enabled}')

        disabled_check = self.driver.find_element(*self.DISABLED_ELE)
        status_disabled = disabled_check.is_enabled()
        print(f'Disabled box status is {status_disabled}')