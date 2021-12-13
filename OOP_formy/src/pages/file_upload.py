"""
File upload page using a png file
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FileUpload(BasePage):
    FILE_UP = (By.ID, 'file-upload-field')

    def upload_file(self):
        file_up = self.driver.find_element(*self.FILE_UP)
        file_up.send_keys('C:/Users/anton/PycharmProjects/Automation_testing/exercices_todo/blue.png')
