"""
Context menu alert window
Interacting with an alert popup
"""

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from OOP_the_internet_herokuapp.src.page.base_page import BasePage


class ContextMenu(BasePage):
    HOTSPOT = (By.ID, 'hot-spot')

    def context_menu(self):
        action = ActionChains(self.driver)
        self.driver.find_element(*self.HOTSPOT)
        action.context_click(self.driver.find_element(*self.HOTSPOT)).perform()
        time.sleep(1.5)
