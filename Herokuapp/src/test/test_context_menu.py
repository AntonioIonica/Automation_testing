"""
Test context menu
asserting if after context clicking, the alert opens
"""

import time, unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from Herokuapp.src.page.context_menu_page import ContextMenu

service = Service('/chromedriver.exe')


class TestContextMenu(unittest.TestCase):
    CONTEXT = (By.XPATH, '//*[@id="content"]/ul/li[7]/a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    def test_context_menu(self):
        self.driver.find_element(*self.CONTEXT).click()
        click_context = ContextMenu(self.driver)
        click_context.context_menu()
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, 'You selected a context menu')
        alert.accept()
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
