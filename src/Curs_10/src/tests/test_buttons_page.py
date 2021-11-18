"""
test button page
"""

import time
import unittest

from selenium.webdriver.common.by import By

from pages.buttons_page import ButtonsPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('C:/Users/anton/PycharmProjects/Automation_testing/src/Curs_10/chromedriver.exe')

class TestButtonsPage(unittest.TestCase):
    BUTTONS_BTN = (By.CSS_SELECTOR, 'body > div > div > li:nth-child(6) > a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://formy-project.herokuapp.com/')
        time.sleep(2)
        self.driver.maximize_window()
        self.driver.find_element(*self.BUTTONS_BTN).click()

    def test_hover_on_buttons(self):
        buttons = ButtonsPage(self.driver)
        buttons.hover_on_buttons()
        time.sleep(1.5)
        self.driver.close()

    def test_click_on_buttons(self):
        buttons = ButtonsPage(self.driver)
        buttons.click_on_buttons()
        time.sleep(1.5)
        self.driver.close()

    def test_click_on_dropdown(self):
        buttons = ButtonsPage(self.driver)
        buttons.click_on_dropdown()
        time.sleep(1.5)
        self.driver.close()

    def tearDown(self) -> None:
        time.sleep(1.5)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
