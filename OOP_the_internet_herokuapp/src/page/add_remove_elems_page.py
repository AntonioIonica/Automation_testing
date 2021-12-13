"""
Add and remove elements
"""
import time

from selenium.webdriver.common.by import By
from OOP_the_internet_herokuapp.src.page.base_page import BasePage


class AddRemove(BasePage):
    ADD_BTN = (By.XPATH, '//*[@id="content"]/div/button')
    DEL_CLASS = (By.CLASS_NAME, 'added-manually')
    DEL_1_BTN = (By.CSS_SELECTOR, '#elements > button:nth-child(1)')
    DEL_2_BTN = (By.CSS_SELECTOR, '#elements > button:nth-child(2)')
    DEL_3_BTN = (By.CSS_SELECTOR, '#elements > button:nth-child(3)')
    DEL_4_BTN = (By.CSS_SELECTOR, '#elements > button:nth-child(4)')
    DEL_5_BTN = (By.CSS_SELECTOR, '#elements > button:nth-child(5)')
    DEL_6_BTN = (By.CSS_SELECTOR, '#elements > button:nth-child(6)')
    DEL_7_BTN = (By.CSS_SELECTOR, '#elements > button:nth-child(7)')
    DEL_8_BTN = (By.CSS_SELECTOR, '#elements > button:nth-child(8)')
    DEL_9_BTN = (By.CSS_SELECTOR, '#elements > button:nth-child(9)')
    DEL_10_BTN = (By.CSS_SELECTOR, '#elements > button:nth-child(10)')

    def add_elements(self):
        add_elems = self.driver.find_element(*self.ADD_BTN)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)

    def del_element(self):
        add_elems = self.driver.find_element(*self.ADD_BTN)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        time.sleep(0.5)
        add_elems.click()
        self.driver.find_element(*self.DEL_1_BTN).click()