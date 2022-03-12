"""
Drag and drop page
"""
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class DragDrop(BasePage):
    DRAGGABLE = (By.XPATH, '//*[@id="image"]/img')
    BOX = (By.ID, 'box')

    def drag_and_drop(self):
        source1 = self.driver.find_element(*self.DRAGGABLE)
        source2 = self.driver.find_element(*self.BOX)
        action = ActionChains(self.driver)
        action.drag_and_drop(source1, source2).perform()
        time.sleep(1)
        time.sleep(1)
