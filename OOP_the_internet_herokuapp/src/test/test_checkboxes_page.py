"""
Testing if there is a selected checkbox by default (The first one)
Checked if the boxes work after I select them
"""

import time, unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from OOP_the_internet_herokuapp.src.page.checkboxes_page import Checkboxes


class TestCheckboxes(unittest.TestCase):
    HEADER = (By.XPATH, '//*[@id="content"]/div/h3')
    NAVI = (By.XPATH, '//*[@id="content"]/ul/li[6]/a')
    CHECKBOX_1 = (By.XPATH, '//*[@id="checkboxes"]/input[1]')
    CHECKBOX_2 = (By.XPATH, '//*[@id="checkboxes"]/input[2]')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.find_element(*self.NAVI).click()
        self.driver.implicitly_wait(5)

    def test_selected_boxes(self):
        box1 = self.driver.find_element(*self.CHECKBOX_1)
        box2 = self.driver.find_element(*self.CHECKBOX_2)
        self.assertFalse(box1.is_selected())
        self.assertFalse(box2.is_selected())
        self.driver.close()

    def test_header(self):
        header = self.driver.find_element(*self.HEADER).text
        self.assertEqual('Checkboxes', header)
        self.driver.close()

    def test_double_click_box1(self):
        boxes = Checkboxes(self.driver)
        boxes.double_click()
        self.driver.implicitly_wait(3)
        box1 = self.driver.find_element(*self.CHECKBOX_1)
        self.assertFalse(box1.is_selected())
        self.driver.close()

    def test_uncheck_box2(self):
        boxes = Checkboxes(self.driver)
        boxes.uncheck_box2()
        self.driver.implicitly_wait(3)
        box2 = self.driver.find_element(*self.CHECKBOX_2)
        self.assertFalse(box2.is_selected())
        self.driver.close()

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
