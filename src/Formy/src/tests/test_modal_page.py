"""
Modal page test
"""

import time, unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pages.modal_page import ModalPage

service = Service('C:/Users/anton/PycharmProjects/Automation_testing/src/Formy/chromedriver.exe')


class TestModalPage(unittest.TestCase):
    MODAL_PAGE = (By.XPATH, '/html/body/div/div/li[10]/a')
    MODAL_TXT = (By.XPATH, '//*[@id="exampleModal"]/div/div/div[2]')
    MODAL_TITLE = (By.XPATH, '//*[@id="exampleModal"]/div/div')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://formy-project.herokuapp.com/')
        time.sleep(2)
        self.driver.maximize_window()
        self.driver.find_element(*self.MODAL_PAGE).click()
        time.sleep(1.5)

    def test_modal_text(self):
        modal = ModalPage(self.driver)
        modal.check_modal_text()
        modal_text = self.driver.find_element(*self.MODAL_TXT).text
        self.assertEqual('Some text here', modal_text)
        time.sleep(1.5)
        self.driver.close()

    def test_click_on_ok(self):
        modal = ModalPage(self.driver)
        modal.click_on_ok()
        modal_title = self.driver.find_element(*self.MODAL_TITLE)
        self.assertFalse(modal_title.is_displayed())
        time.sleep(1.5)
        self.driver.close()

    def test_click_on_close(self):
        modal = ModalPage(self.driver)
        modal.click_on_close()
        time.sleep(1.5)
        modal_title = self.driver.find_element(*self.MODAL_TITLE)
        self.assertFalse(modal_title.is_displayed())
        time.sleep(1.5)
        self.driver.close()

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
