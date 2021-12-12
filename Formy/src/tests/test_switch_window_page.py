"""
Test switch window page and alert
"""

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pages.switch_window_page import SwitchWindow
service = Service('/chromedriver.exe')

class TestSwitchWindow(unittest.TestCase):
    SWITCH_WINDOW_BTN = (By.XPATH, '/html/body/div/div/li[13]/a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.get('https://formy-project.herokuapp.com/')
        driver.maximize_window()
        time.sleep(1.5)
        driver.find_element(*self.SWITCH_WINDOW_BTN).click()
        time.sleep(1.5)

    def test_new_tab(self):
        alert_button = SwitchWindow(self.driver)
        alert_button.click_on_alert()
        time.sleep(1.5)
        self.driver.close()

    def test_switch_window(self):
        switch_window = SwitchWindow(self.driver)
        switch_window.click_new_tab()
        time.sleep(1.5)
        self.driver.close()

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()