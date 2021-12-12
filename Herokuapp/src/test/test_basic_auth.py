"""
Testing basic authentification using browser alert type login
user, password = admin
"""
import time, unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Herokuapp.src.page.basic_auth import BasicAuth

service = Service('/chromedriver.exe')


class TestBasicAuth(unittest.TestCase):
    AUTH = (By.XPATH, '//*[@id="content"]/ul/li[3]/a')
    CONGRAT_MSG = (By.XPATH, '//*[@id="content"]/div/p')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    def test_basic_auth(self):
        self.driver.find_element(*self.AUTH).click()
        login = BasicAuth(self.driver)
        login.basic_auth()
        self.driver.implicitly_wait(3)
        congrats_msg = self.driver.find_element(*self.CONGRAT_MSG)
        self.assertTrue(congrats_msg.is_displayed())
        time.sleep(1.5)
        self.driver.back()
        self.driver.back()

if __name__ == '__main__':
    unittest.main()