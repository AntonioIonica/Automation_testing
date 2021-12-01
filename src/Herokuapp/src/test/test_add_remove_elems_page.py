"""
Testing add and remove elements
adding 10 buttons, then deleting them
asserting if they delete
asserting if they appear after adding them
"""

import time, unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from page.add_remove_elems_page import AddRemove

service = Service('C:/Users/anton/PycharmProjects/Automation_testing/src/Herokuapp/chromedriver.exe')


class TestAddRemove(unittest.TestCase):
    ADD_BTN = (By.XPATH, '//*[@id="content"]/div/button')
    DEL_CLASS = (By.CLASS_NAME, 'added-manually')
    DEL_1_BTN = (By.XPATH, '//*[@id="elements"]/button[1]')
    DEL_9_BTN = (By.XPATH, '//*[@id="elements"]/button[9]')
    NAVI = (By.XPATH, '//*[@id="content"]/ul/li[2]/a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_add_elements(self):
        self.driver.find_element(*self.NAVI).click()
        self.driver.implicitly_wait(5)
        self.assertTrue(self.driver.find_element(*self.ADD_BTN).is_displayed())
        elements = AddRemove(self.driver)
        elements.add_elements()
        self.driver.implicitly_wait(3)
        self.assertTrue(self.driver.find_element(*self.DEL_9_BTN).is_displayed())
        self.assertTrue(self.driver.find_element(*self.DEL_1_BTN).is_displayed())
        self.driver.close()

    def test_del_elements(self):
        self.driver.find_element(*self.NAVI).click()
        self.driver.implicitly_wait(5)
        elements = AddRemove(self.driver)
        elements.del_element()
        self.assertTrue(self.driver.find_element(*self.DEL_9_BTN).is_displayed())
        self.driver.close()

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')