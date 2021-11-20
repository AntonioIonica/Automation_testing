"""
Modal page
"""

from pages.base_page import BasePage
import time
from selenium.webdriver.common.by import By


class ModalPage(BasePage):
    MODAL_BTN = (By.ID, 'modal-button')
    CLOSE_BTN = (By.ID, 'close-button')
    OK_BTN = (By.ID, 'ok-button')

    def click_on_ok(self):
        modal_btn = self.driver.find_element(*self.MODAL_BTN)
        modal_btn.click()
        time.sleep(1.5)
        ok_btn = self.driver.find_element(*self.OK_BTN)
        ok_btn.click()

    def click_on_close(self):
        modal_btn = self.driver.find_element(*self.MODAL_BTN)
        modal_btn.click()
        time.sleep(1.5)
        close_btn = self.driver.find_element(*self.CLOSE_BTN)
        close_btn.click()

    def check_modal_text(self):
        modal_btn = self.driver.find_element(*self.MODAL_BTN)
        modal_btn.click()
        time.sleep(1.5)
