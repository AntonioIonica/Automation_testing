"""
Switch window and alert window
"""
from pages.base_page import BasePage
import time
from selenium.webdriver.common.by import By


class SwitchWindow(BasePage):
    SWITCH_WINDOW_BTN = (By.ID, 'new-tab-button')
    ALERT_BTN = (By.ID, 'alert-button')

    def click_new_tab(self):
        new_tab = self.driver.find_element(*self.SWITCH_WINDOW_BTN)
        new_tab.click()
        time.sleep(1.5)
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            time.sleep(1)
            print(f'The current page title is {self.driver.title}')

    def click_on_alert(self):
        alert_button = self.driver.find_element(*self.ALERT_BTN)
        alert_button.click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
