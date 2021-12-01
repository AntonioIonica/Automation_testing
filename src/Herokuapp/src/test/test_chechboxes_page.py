"""
Testing if there is a selected checkbox by default (The first one)
Checked if the boxes work after I select them
"""

import time, unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from page.chechboxes_page import Checkboxes

service = Service('C:/Users/anton/PycharmProjects/Automation_testing/src/Herokuapp/chromedriver.exe')


class TestCheckboxes(unittest.TestCase):
    HEADER = (By.XPATH, '//*[@id="content"]/div/h3')
    NAVI = (By.XPATH, '//*[@id="content"]/ul/li[6]/a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_selected(self):
       self.assertFalse(self.