"""
Context menu alert window
"""

import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('//chromedriver.exe')


class TestContext(unittest.TestCase):
    CONTEXT = (By.XPATH, '//*[@id="content"]/ul/li[7]/a')
    HOTSPOT = (By.ID, 'hot-spot')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_context_menu(self):
        self.driver.find_element(*self.CONTEXT).click()
        self.driver.implicitly_wait(3)
        action = ActionChains(self.driver)
        action.context_click(self.driver.find_element(*self.HOTSPOT)).perform()
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, 'You selected a context menu')
        alert.accept()
        time.sleep(1.5)
        self.driver.close()

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()
