"""
Enabled and disabled elements
checking using is_enabled()
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class EnabledDisabledEle(BasePage):
    ENABLED_ELE = (By.ID, 'input')
    DISABLED_ELE = (By.ID, 'disabledInput')

    def enabled_box(self):
        enabled_box = self.driver.find_element(*self.ENABLED_ELE)
        enabled_box.clear()
        enabled_box.send_keys('Romania')

    def disabled_box(self):
        self.driver.find_element(*self.DISABLED_ELE).click()

