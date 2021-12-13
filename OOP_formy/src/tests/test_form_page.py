"""
Executing the typed data and asserting if the form can be submitted
"""

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.form_page import FormPage


class TestFormPage(unittest.TestCase):
    SUCCESS_ALERT = (By.XPATH, '/html/body/div/div')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://formy-project.herokuapp.com/form')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

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
        success = self.driver.find_element(*self.SUCCESS_ALERT).text
        if 'The form was successfully submitted!' in success:
            assert True, 'Test passed!'
        else:
            assert False, 'Test Failed'
        time.sleep(1.5)

    def tearDown(self) -> None:
        time.sleep(1.5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
