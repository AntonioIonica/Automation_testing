"""
Radio button page test
"""

import time, unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pages.radio_button_page import RadioButtonPage

service = Service('C:/Users/anton/PycharmProjects/Automation_testing/src/Formy/chromedriver.exe')


class TestRadioButton(unittest.TestCase):
    RADIO_BTN = (By.XPATH, '/html/body/div/div/li[12]/a')
    RADIO_BTN_1 = (By.ID, 'radio-button-1')
    RADIO_BTN_2 = (By.XPATH, '/html/body/div/div[2]/input')
    RADIO_BTN_3 = (By.XPATH, '/html/body/div/div[3]/input')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://formy-project.herokuapp.com/')
        time.sleep(2)
        self.driver.maximize_window()
        self.driver.find_element(*self.RADIO_BTN).click()
        time.sleep(1.5)

    def test_btn_1_displayed(self):
        btn_1 = self.driver.find_element(*self.RADIO_BTN_1)
        self.assertTrue(btn_1.is_selected())
        time.sleep(1)
        self.driver.quit()

    def test_btn_3(self):
        radio_click = RadioButtonPage(self.driver)
        radio_click.click_on_btn_3()

        btn_1 = self.driver.find_element(*self.RADIO_BTN_1)
        btn_2 = self.driver.find_element(*self.RADIO_BTN_2)
        btn_3 = self.driver.find_element(*self.RADIO_BTN_3)

        self.assertFalse(btn_1.is_selected())
        time.sleep(1)
        self.assertFalse(btn_2.is_selected())
        time.sleep(1)
        self.assertTrue(btn_3.is_selected())
        time.sleep(1)
        self.driver.close()

    def test_btn_2(self):
        radio_click = RadioButtonPage(self.driver)
        radio_click.click_on_btn_2()

        btn_1 = self.driver.find_element(*self.RADIO_BTN_1)
        btn_2 = self.driver.find_element(*self.RADIO_BTN_2)
        btn_3 = self.driver.find_element(*self.RADIO_BTN_3)

        self.assertFalse(btn_1.is_selected())
        time.sleep(1)
        self.assertTrue(btn_2.is_selected())
        time.sleep(1)
        self.assertFalse(btn_3.is_selected())
        time.sleep(1)
        self.driver.close()

    def test_btn_1(self):
        radio_click = RadioButtonPage(self.driver)
        radio_click.click_on_btn_1()

        btn_1 = self.driver.find_element(*self.RADIO_BTN_1)
        btn_2 = self.driver.find_element(*self.RADIO_BTN_2)
        btn_3 = self.driver.find_element(*self.RADIO_BTN_3)

        self.assertTrue(btn_1.is_selected())
        time.sleep(1)
        self.assertFalse(btn_2.is_selected())
        time.sleep(1)
        self.assertFalse(btn_3.is_selected())
        time.sleep(1)
        self.driver.close()

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()