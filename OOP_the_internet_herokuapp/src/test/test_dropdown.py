"""
Testing dropdown select option 1 and option 2
"""

import time, unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from OOP_the_internet_herokuapp.src.page.dropdown_page import DropDown


class TestDropdown(unittest.TestCase):
    NAVI = (By.XPATH, '//*[@id="content"]/ul/li[11]/a')
    DROP_MENU = (By.ID, 'dropdown')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.find_element(*self.NAVI).click()
        self.driver.implicitly_wait(5)

    def test_dropdown_1(self):
        dropdown = DropDown(self.driver)
        dropdown.click_on_option_1()
        time.sleep(2)
        self.driver.close()

    def test_dropdown_2(self):
        dropdown = DropDown(self.driver)
        dropdown.click_on_option_2()
        time.sleep(2)
        self.driver.close()

    def tearDown(self) -> None:
        time.sleep(1.5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
