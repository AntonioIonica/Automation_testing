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

    def test_address_and_title(self):
        auto_page = AutocompletePage(self.driver)
        self.assertEqual(auto_page.title_page(), 'Formy')
        auto_page.enter_adr()
        time.sleep(1.5)
        self.driver.close()

    def test_street_1(self):
        auto_page = AutocompletePage(self.driver)
        auto_page.enter_str_1()
        time.sleep(1.5)
        self.driver.close()

    def test_street_2(self):
        auto_page = AutocompletePage(self.driver)
        auto_page.enter_str_2()
        time.sleep(1.5)
        self.driver.close()

    def test_city(self):
        auto_page = AutocompletePage(self.driver)
        auto_page.enter_city()
        time.sleep(1.5)
        self.driver.close()

    def test_state(self):
        auto_page = AutocompletePage(self.driver)
        auto_page.enter_state()
        time.sleep(1.5)
        self.driver.close()

    def test_zip(self):
        auto_page = AutocompletePage(self.driver)
        auto_page.enter_zip()
        time.sleep(1.5)
        self.driver.close()

    def test_country(self):
        auto_page = AutocompletePage(self.driver)
        auto_page.enter_country()
        time.sleep(1.5)
        self.driver.close()

    def tearDown(self) -> None: # ruleaza la fiecare metoda, testcase, la final
        time.sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
