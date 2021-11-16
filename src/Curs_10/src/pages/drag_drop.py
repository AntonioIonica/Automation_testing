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
        driver = self.driver
        driver.switch_to.frame(0)
        source1 = driver.find_element(*self.DRAGGABLE)
        source2 = driver.find_element(*self.BOX)
        action = ActionChains(driver)
        action.drag_and_drop_by(source1, source2).perform()
        time.sleep(5)