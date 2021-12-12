"""
Login on Form authentification page
taking the user and the password from the text
(italic words)
"""

from selenium.webdriver.common.by import By
from Herokuapp.src.page.base_page import BasePage


class FormAuth(BasePage):
    USR = (By.ID, 'username')
    PWD = (By.ID, 'password')
    LOGIN_BTN = (By.XPATH, '//*[@id="login"]/button')
    TEXT_AUTH = (By.XPATH, '//*[@id="content"]/div/h4')

    def invalid_login(self):
        self.driver.find_element(*self.USR).send_keys('admin')
        self.driver.find_element(*self.PWD).send_keys('test123')
        self.driver.find_element(*self.LOGIN_BTN).click()
        self.driver.implicitly_wait(3)

    def valid_login(self):
        auth_text = self.driver.find_element(*self.TEXT_AUTH).text
        text_list = auth_text.split('.')[1].split()
        print(text_list)
        usr = [text_list[i + 1] for i in range(0, len(text_list)) if text_list[i] == 'Enter']
        pwd = [text_list[i + 1] for i in range(0, len(text_list)) if text_list[i] == 'and']
        self.driver.find_element(*self.USR).send_keys(usr)
        self.driver.find_element(*self.PWD).send_keys(pwd)
        self.driver.find_element(*self.LOGIN_BTN).click()
        self.driver.implicitly_wait(3)
