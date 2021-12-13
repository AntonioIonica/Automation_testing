"""
Radio button page
clicking them in different order
"""

from pages.base_page import BasePage
import time
from selenium.webdriver.common.by import By


class RadioButtonPage(BasePage):
    RADIO_BTN_1 = (By.ID, 'radio-button-1')
    RADIO_BTN_2 = (By.XPATH, '/html/body/div/div[2]/input')
    RADIO_BTN_3 = (By.XPATH, '/html/body/div/div[3]/input')

    def click_on_btn_3(self):
        btn_1 = self.driver.find_element(*self.RADIO_BTN_1)
        btn_2 = self.driver.find_element(*self.RADIO_BTN_2)
        btn_3 = self.driver.find_element(*self.RADIO_BTN_3)

        btn_2.click()
        time.sleep(1)
        btn_1.click()
        time.sleep(1)
        btn_3.click()

    def click_on_btn_2(self):
        btn_1 = self.driver.find_element(*self.RADIO_BTN_1)
        btn_2 = self.driver.find_element(*self.RADIO_BTN_2)
        btn_3 = self.driver.find_element(*self.RADIO_BTN_3)

        btn_1.click()
        time.sleep(1)
        btn_3.click()
        time.sleep(1)
        btn_2.click()

    def click_on_btn_1(self):
        btn_1 = self.driver.find_element(*self.RADIO_BTN_1)
        btn_2 = self.driver.find_element(*self.RADIO_BTN_2)
        btn_3 = self.driver.find_element(*self.RADIO_BTN_3)

        btn_3.click()
        time.sleep(1)
        btn_2.click()
        time.sleep(1)
        btn_1.click()
