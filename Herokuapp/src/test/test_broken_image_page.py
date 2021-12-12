"""
Testing broken images
"""

import time, unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from Herokuapp.src.page.broken_images_page import BrokenImage

service = Service('/chromedriver.exe')


class TestBrokenImage(unittest.TestCase):
    NAVI = (By.XPATH, '//*[@id="content"]/ul/li[4]/a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    def test_broken_images(self):
        self.driver.find_element(*self.NAVI).click()
        broken = BrokenImage(self.driver)
        broken.broken_images()
        self.driver.close()


if __name__ == '__main__':
    unittest.main()