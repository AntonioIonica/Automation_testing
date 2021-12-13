"""
Alert interaction on The-internet.herokuapp website
using switch_to.alert method
"""

import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestContext(unittest.TestCase):
    CONTEXT = (By.XPATH, '//*[@id="content"]/ul/li[7]/a')
    HOTSPOT = (By.ID, 'hot-spot')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
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


if __name__ == '__main__':
    unittest.main()
