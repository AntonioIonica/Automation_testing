"""
Test enabled and disabled inputs
"""

import time, unittest
from selenium.webdriver.common.by import By
from pages.enab_disab import EnabledDisabledEle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('C:/Users/anton/PycharmProjects/Automation_testing/src/Formy/chromedriver.exe')


class TestEnabledDisabledEle(unittest.TestCase):
    ENAB_DISAB_ELEMS_BTN = (By.CSS_SELECTOR, 'body > div > div > li:nth-child(11) > a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://formy-project.herokuapp.com/')
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element(*self.ENAB_DISAB_ELEMS_BTN).click()

    def test_disabled(self):
        status = EnabledDisabledEle(self.driver)
        status.disabled_box()
        disable_box = self.driver.find_element(By.ID, 'disabledInput')
        self.assertFalse(disable_box.is_enabled())
        print(f'Status of Disabled Box is {disable_box.is_displayed}')
        time.sleep(1.5)
        self.driver.close()

    def test_enabled(self):
        status = EnabledDisabledEle(self.driver)
        status.enabled_box()
        enable_box = self.driver.find_element(By.ID, 'input')
        self.assertTrue(enable_box.is_enabled())
        time.sleep(1.8)
        print(f'Status of Enabled Box is {enable_box.is_displayed()}')
        time.sleep(1.5)
        self.driver.close()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
