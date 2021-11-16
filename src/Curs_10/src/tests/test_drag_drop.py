"""
Drag and drop testing
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from pages.drag_drop import DragDrop

service = Service('C:/Users/anton/PycharmProjects/Automation_testing/src/Curs_10/chromedriver.exe')

class TestDragDrop(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://formy-project.herokuapp.com/dragdrop')
        self.driver.maximize_window()

    def test_drag_drop(self):
        drop = DragDrop(self.driver)
        drop.drag_and_drop()

    def tearDown(self) -> None:
        time.sleep(1.5)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()