"""
Authentification in an alert popup using admin/admin creds

"""
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestAuth(unittest.TestCase):
    AUTH = (By.XPATH, '//*[@id="content"]/ul/li[3]/a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.maximize_window()
        driver.implicitly_wait(5)

    def test_auth(self):
        self.driver.find_element(*self.AUTH).click()
        usr = 'admin'
        pwd = 'admin'
        time.sleep(2)
        self.driver.get('https://' + usr + ':' + pwd + '@' + 'the-internet.herokuapp.com/basic_auth')
        self.assertEqual(self.driver.title, 'The Internet')
        time.sleep(2)
        self.driver.back()
        self.driver.back()

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
