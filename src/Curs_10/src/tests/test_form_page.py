"""
Form page testcases
"""

import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pages.form_page import FormPage
service = Service('C:/Users/anton/PycharmProjects/Automation_testing/src/Curs_10/chromedriver.exe')

class TestFormPage(unittest.TestCase):
    SUCCES_ALERT = (By.CLASS_NAME, 'alert alert-success')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://formy-project.herokuapp.com/form')
        self.driver.maximize_window()
        time.sleep(2)

    def test_form_page(self):
        form_page = FormPage(self.driver)
        self.assertTrue(form_page.header_name())
        form_page.click_on_f_name()
        time.sleep(1.5)
        form_page.click_on_l_name()
        time.sleep(1.5)
        form_page.click_on_job_title()
        time.sleep(1.5)
        form_page.click_on_education_junior()
        time.sleep(1.5)
        form_page.click_on_sexual_identification()
        time.sleep(1.5)
        form_page.click_on_experience()
        time.sleep(1.5)
        form_page.enter_date()
        time.sleep(1.5)
        form_page.enter_date()
        time.sleep(1.5)
        form_page.click_on_submit()

        time.sleep(1.5)
        succes = self.driver.find_element(*self.SUCCES_ALERT).text
        if 'The form was successfully submitted!' in succes:
            print('Test passed!')
        else:
            print('Test Failed!')
        time.sleep(1.5)

    def tearDown(self) -> None:
        time.sleep(1.5)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()