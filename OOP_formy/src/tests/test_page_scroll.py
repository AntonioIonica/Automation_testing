"""
Test switch window page and alert
"""

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.page_scroll import PageScroll


class TestPageScroll(unittest.TestCase):
    PAGE_SCROLL_BTN = (By.XPATH, '/html/body/div/div/li[11]/a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.get('https://formy-project.herokuapp.com/')
        driver.maximize_window()
        time.sleep(1.5)
        driver.find_element(*self.PAGE_SCROLL_BTN).click()
        time.sleep(1.5)

    def test_scroll_down(self):
        scroll = PageScroll(self.driver)
        scroll.page_scroll()
        scroll.insert_name()
        time.sleep(1.5)
        scroll.date_input()
        full_name = self.driver.find_element(By.ID, 'name').text
        date_input = self.driver.find_element(By.ID, 'date').text
        self.assertIn('Antonio', full_name)
        self.assertIn('07/18/1996', date_input)

    def tearDown(self) -> None:
        time.sleep(1.5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
