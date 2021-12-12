"""
login oop style
"""
import unittest

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('//chromedriver.exe')


class TestLogin(unittest.TestCase):
    navi = (By.CSS_SELECTOR, '#content > ul > li:nth-child(21) > a')
    usr = (By.ID, 'username')
    pwd = (By.ID, 'password')
    login_btn = (By.CSS_SELECTOR, '#login > button')
    logout_btn = (By.CSS_SELECTOR, '#content > div > a')
    error_login = (By.ID, 'flash-messages')
    TEXT_AUTH = (By.XPATH, '//*[@id="content"]/div/h4')

    def setUp(self) -> None:
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

    def test_auth_auto(self):
        global user
        global password
        self.driver.find_element(*self.navi).click()
        self.driver.implicitly_wait(5)  # va astepta doar cat e nevoie
        auth_text = self.driver.find_element(*self.TEXT_AUTH).text
        print(auth_text)
        text_lst = auth_text.split('.')[1].split()
        print(text_lst)
        # user = ''
        # password = ''
        for i in range(0, len(text_lst)):
            if text_lst[i] == 'Enter':
                user = text_lst[i + 1]
            if text_lst[i] == 'and':
                password = text_lst[i + 1]
        self.driver.find_element(*self.usr).send_keys(user)
        self.driver.find_element(*self.pwd).send_keys(password)

        # user_text2 = [text_lst[i + 1] for i in range(0, len(text_lst)) if text_lst[i] == 'Enter']

    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
