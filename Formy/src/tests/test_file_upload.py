"""
Test file upload case
"""

import time, unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.file_upload import FileUpload
from selenium.webdriver.chrome.service import Service

service = Service('/chromedriver.exe')


class TestFileUpload(unittest.TestCase):
    FILE_UPLOAD_BTN = (By.CSS_SELECTOR, 'body > div > div > li:nth-child(12) > a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://formy-project.herokuapp.com/')
        self.driver.maximize_window()

    def test_file_upload(self):
        self.driver.find_element(*self.FILE_UPLOAD_BTN).click()
        time.sleep(1.5)
        upload = FileUpload(self.driver)
        upload.upload_file()

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
