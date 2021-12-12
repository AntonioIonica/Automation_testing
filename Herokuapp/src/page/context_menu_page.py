"""
Context menu alert window
"""

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Herokuapp.src.page.base_page import BasePage


class ContextMenu(BasePage):
    HOTSPOT = (By.ID, 'hot-spot')

    def context_menu(self):
        action = ActionChains(self.driver)
        self.driver.find_element(*self.HOTSPOT)
        action.context_click(self.driver.find_element(*self.HOTSPOT)).perform()
        time.sleep(1.5)
