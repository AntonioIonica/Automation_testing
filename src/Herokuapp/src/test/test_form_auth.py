"""

"""

from selenium import webdriver
import unittest, time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from page.form_auth_page import FormAuth

service = Service('C:/Users/anton/PycharmProjects/Automation_testing/src/Herokuapp/chromedriver.exe')


class TestFormAuth(unittest.TestCase):
    LOGOUT_BTN = (By.XPATH, '//*[@id="content"]/div/a')
    ERROR_LOGIN = (By.ID, 'flash-messages')
    NAVI = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    SUCCES_LOGIN = (By.ID, 'flash')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    def test_invalid_login(self):
        self.driver.find_element(*self.NAVI).click()
        self.driver.implicitly_wait(3)
        login = FormAuth(self.driver)
        login.invalid_login()
        alert = self.driver.find_element(*self.ERROR_LOGIN).text
        self.assertIn('Your username is invalid', alert)
        self.driver.close()

    def test_valid_login(self):
        self.driver.find_element(*self.NAVI).click()
        self.driver.implicitly_wait(3)
        login = FormAuth(self.driver)
        login.valid_login()
        time.sleep(2.5)
        succes_login = self.driver.find_element(*self.SUCCES_LOGIN).text
        self.assertIn('You logged into a secure area!', succes_login)
        self.driver.find_element(*self.LOGOUT_BTN).click()
        time.sleep(2)
        logout_msg = self.driver.find_element(By.XPATH, '//*[@id="flash"]').text
        self.assertIn('You logged out of the secure area!\n×', logout_msg)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()