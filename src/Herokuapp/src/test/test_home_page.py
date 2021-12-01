"""
Home page of Herokuapp
clicking on buttons and coming back to home page
"""

import time, unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from page.home_page import HomePage

service = Service('C:/Users/anton/PycharmProjects/Automation_testing/src/Herokuapp/chromedriver.exe')


class TestHomePage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_title_page(self):
        home_page = HomePage(self.driver)
        self.assertEqual(home_page.title_page(), 'The Internet')

    def test_click_on_ab_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_ab_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_add_remove_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_add_remove_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_basic_auth_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_basic_auth_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_broken_img_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_broken_img_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_challenging_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_challenging_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_check_box_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_check_box_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_context_menu_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_context_menu_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_digest_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_digest_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_dissap_elements_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_dissap_elements_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_drag_drop_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_drag_drop_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_dropdown_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_dropdown_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_dynamic_content_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_dynamic_content_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_dynamic_controls_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_dynamic_controls_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_dynamic_loading_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_dynamic_loading_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_entry_ad_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_entry_ad_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_exit_intent_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_exit_intent_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_file_down_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_file_down_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_file_up_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_file_up_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_floating_menu_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_floating_menu_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_forgot_pass_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_forgot_pass_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_form_auth_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_form_auth_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_frames_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_frames_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_geolocation_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_geolocation_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_horizontal_slider_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_horizontal_slider_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_hovers_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_hovers_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_infinite_scroll_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_infinite_scroll_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_inputs_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_inputs_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_jquery_ui_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_jquery_ui_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_js_alerts_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_js_alerts_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_js_onload_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_js_onload_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_key_presses_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_key_presses_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_large_deep_dom_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_large_deep_dom_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_multiple_windows_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_multiple_windows_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_nested_frames_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_nested_frames_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_notification_messages_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_notification_messages_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_redirect_link_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_redirect_link_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_secure_download_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_secure_download_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_shadow_dom_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_shadow_dom_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_shifting_content_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_shifting_content_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_slow_resources_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_slow_resources_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_sortable_data_tables_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_sortable_data_tables_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_status_codes_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_status_codes_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_typos_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_typos_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def test_click_on_wysiwyg_editor_btn(self):
        home_page = HomePage(self.driver)
        home_page.click_on_wysiwyg_editor_btn()
        self.driver.implicitly_wait(2)
        self.driver.back()
        header_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        self.assertEqual(header_2, 'Available Examples')
        self.driver.close()

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
