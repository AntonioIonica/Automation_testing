"""
Admin login page objects using the given credentials
"""
import time
from selenium.webdriver.common.by import By


class AdminLoginPage:
    TEXTBOX_EMAIL = (By.ID, 'Email')
    TEXTBOX_PWD = (By.ID, 'Password')
    BTN_LOGIN = (By.XPATH, "//button[@type='submit']")
    BTN_LOGOUT = (By.XPATH, "//a[@href='/logout']")

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email_info):
        email_box = self.driver.find_element(*self.TEXTBOX_EMAIL)
        email_box.clear()
        email_box.send_keys(email_info)

    def set_pwd(self, pwd_info):
        pwd_box = self.driver.find_element(*self.TEXTBOX_PWD)
        pwd_box.clear()
        time.sleep(2)
        pwd_box.send_keys(pwd_info)

    def click_login(self):
        self.driver.find_element(*self.BTN_LOGIN).click()

    def click_logout(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.BTN_LOGOUT).click()
