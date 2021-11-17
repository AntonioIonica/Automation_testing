"""
Test enabled and disabled inputs
"""

import time, unittest
from selenium.webdriver.common.by import By
from pages.enab_disab import EnabledDisabledEle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('C:/Users/anton/PycharmProjects/Automation_testing/src/Curs_10/chromedriver.exe')

class TestEnabledDisabledEle(unittest.TestCase):
    ENAB_DISAB_ELEMS_BTN = (By.CSS_SELECTOR, 'body > div > div > li:nth-child(11) > a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://formy-project.herokuapp.com/')
        self.driver.maximize_window()
        time.sleep(2)

    def test_check_status(self):
        self.driver.find_element(*self.ENAB_DISAB_ELEMS_BTN).click()
        time.sleep(2)
        status = EnabledDisabledEle(self.driver)
        status.disabled_check()

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
