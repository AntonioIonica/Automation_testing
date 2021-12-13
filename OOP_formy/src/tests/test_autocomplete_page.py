"""
Testing only to ensure that typing some info works, but autocomplete from googlemaps isn't working anymore
"""

import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.autocomplete_page import AutocompletePage


class TestAutocomplete(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://formy-project.herokuapp.com/autocomplete')
        self.driver.maximize_window()

    def test_addresses_and_title(self):
        auto_page = AutocompletePage(self.driver)
        self.assertEqual(auto_page.title_page(), 'Formy')
        auto_page.enter_adr()
        auto_page.enter_str_1()
        auto_page.enter_str_2()
        auto_page.enter_city()
        auto_page.enter_state()
        auto_page.enter_zip()
        auto_page.enter_country()
        time.sleep(1.5)
        self.driver.close()

    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
