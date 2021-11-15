"""
home page testcases
"""

import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.home_page import HomePage

service = Service('C:/Users/anton/PycharmProjects/Automation_testing/src/Curs_10/chromedriver.exe')

class TestHomePage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://formy-project.herokuapp.com/')
        self.driver.maximize_window()
        time.sleep(2)

    def test_buttons(self):
        home_page = HomePage(self.driver)

        home_page.click_on_autocomplete_btn()
        time.sleep(1.5)

        home_page.click_on_buttons_btn()
        time.sleep(1.5)

        home_page.click_on_checkbox_btn()
        time.sleep(1.5)

        home_page.click_on_datepicker_btn()
        time.sleep(1.5)

        home_page.click_on_drag_and_drop_btn()
        time.sleep(1.5)

        home_page.click_on_dropdown_btn()
        time.sleep(1.5)

        home_page.click_on_enab_disab_elems_btn()
        time.sleep(1.5)

        home_page.click_on_file_upload_btn()
        time.sleep(1.5)

        home_page.click_on_key_mouse_press_btn()
        time.sleep(1.5)

        home_page.click_on_modal_btn()
        time.sleep(1.5)

        home_page.click_on_page_scroll_btn()
        time.sleep(1.5)

        home_page.click_on_radio_btn()
        time.sleep(1.5)

        home_page.click_on_switch_window_btn()
        time.sleep(1.5)

        home_page.click_on_complete_web_form_btn()
        time.sleep(1.5)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()