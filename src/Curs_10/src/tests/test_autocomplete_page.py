"""
Where the testcases appear from autocomplete
"""

import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.autocomplete_page import AutocompletePage

service = Service('C:/Users/anton/PycharmProjects/Automation_testing/src/Curs_10/chromedriver.exe')

class TestAutocomplete(unittest.TestCase):

    def setUp(self) -> None: #setUp ruleaza inainte de fiecare testcase, la fiecare!
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://formy-project.herokuapp.com/autocomplete')
        self.driver.maximize_window()

    # aici vin test caseurile

    def test_address_and_street_1(self):
        auto_page = AutocompletePage(self.driver)
        self.assertEqual(auto_page.title_page(), 'Formy')
        auto_page.enter_adr()
        auto_page.enter_str_1()
        auto_page.enter_str_2()
        auto_page.enter_city()
        auto_page.enter_state()
        auto_page.enter_zip()
        auto_page.enter_country()


    def tearDown(self) -> None: # ruleaza la fiecare metoda, testcase, la final
        time.sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
