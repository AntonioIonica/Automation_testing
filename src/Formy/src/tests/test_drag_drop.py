"""
Drag and drop testing
"""

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from pages.drag_drop import DragDrop

service = Service('C:/Users/anton/PycharmProjects/Automation_testing/src/Formy/chromedriver.exe')


class TestDragDrop(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://formy-project.herokuapp.com/dragdrop')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def test_drag_drop(self):
        drop = DragDrop(self.driver)
        drop.drag_and_drop()
        check_drag = self.driver.find_element(By.XPATH, '//*[@id="box"]/p').text
        time.sleep(2)
        self.assertNotEqual(check_drag, 'Drop here')
        time.sleep(1.5)
        self.driver.close()

    def tearDown(self) -> None:
        time.sleep(1.5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
