"""
Page scroll and form page
Scroll to full_name element and entering given data
"""
from pages.base_page import BasePage
import time
from selenium.webdriver.common.by import By


class PageScroll(BasePage):
    FULLNAME = (By.ID, 'name')
    DATE = (By.ID, 'date')

    def page_scroll(self):
        full_name = self.driver.find_element(*self.FULLNAME)
        time.sleep(1.5)
        self.driver.execute_script('arguments[0].scrollIntoView();', full_name)
        time.sleep(1.5)

    def insert_name(self):
        full_name = self.driver.find_element(*self.FULLNAME)
        full_name.clear()
        full_name.send_keys('Antonio')

    def date_input(self):
        date_input = self.driver.find_element(*self.DATE)
        time.sleep(1.5)
        date_input.clear()
        time.sleep(1.5)
        date_input.send_keys('07/18/1996')