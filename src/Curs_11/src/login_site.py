"""
login oop stile
"""
import unittest

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service = Service('C:/Users/anton/PycharmProjects/Automation_testing/src/Curs_10/chromedriver.exe')

class TestLogin(unittest.TestCase):
    navi = (By.CSS_SELECTOR, '#content > ul > li:nth-child(21) > a')
    usr = (By.ID, 'username')
    pwd = (By.ID, 'password')
    login_btn = (By.CSS_SELECTOR, '#login > button')
    logout_btn = (By.CSS_SELECTOR, '#content > div > a')
    error_login = (By.ID, 'flash-messages')

    def setUp(self) -> None:  # uittest.testcase
        self.driver = webdriver.Chrome(service=service)

        self.driver.maximize_window()
        self.driver.get('https://the-internet.herokuapp.com/')
        time.sleep(2)

    def test_invalid_login(self):
        self.driver.find_element(*self.navi).click()
        time.sleep(2)
        self.driver.find_element(*self.usr).send_keys('orice')
        time.sleep(2)
        self.driver.find_element(*self.pwd).send_keys('ptest')
        time.sleep(2)
        self.driver.find_element(*self.login_btn).click()
        alerta = self.driver.find_element(*self.error_login).text
        if 'Your username is invalid' in alerta:
            print('Test invalid login passed')
        time.sleep(2)

    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()