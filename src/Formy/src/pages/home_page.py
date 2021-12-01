"""
Home page-Formy
Clicking on buttons
"""

import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    AUTOCOMPLETE_BTN = (By.XPATH, '/html/body/div/div/li[1]/a')
    BUTTONS_BTN = (By.XPATH, '/html/body/div/div/li[2]/a')
    CHECKBOX_BTN = (By.XPATH, '/html/body/div/div/li[3]/a')
    DATEPICKER_BTN = (By.XPATH, '/html/body/div/div/li[4]/a')
    DRAG_AND_DROP_BTN = (By.XPATH, '/html/body/div/div/li[5]/a')
    DROPDOWN_BTN = (By.XPATH, '/html/body/div/div/li[6]/a')
    ENAB_DISAB_ELEMS_BTN = (By.XPATH, '/html/body/div/div/li[7]/a')
    FILE_UPLOAD_BTN = (By.XPATH, '/html/body/div/div/li[8]/a')
    KEY_MOUSE_PRESS_BTN = (By.XPATH, '/html/body/div/div/li[9]/a')
    MODAL_BTN = (By.XPATH, '/html/body/div/div/li[10]/a')
    PAGE_SCROLL_BTN = (By.XPATH, '/html/body/div/div/li[11]/a')
    RADIO_BTN = (By.XPATH, '/html/body/div/div/li[12]/a')
    SWITCH_WINDOW_BTN = (By.XPATH, '/html/body/div/div/li[13]/a')
    COMPLETE_WEB_FORM_BTN = (By.XPATH, '/html/body/div/div/li[14]/a')
    LOGO = (By.ID, 'logo')

    def click_on_autocomplete_btn(self):
        self.driver.find_element(*self.AUTOCOMPLETE_BTN).click()
        # time.sleep(1.5)
        print('I clicked on Autocomplete!')

    def click_on_buttons_btn(self):
        self.driver.find_element(*self.BUTTONS_BTN).click()
        # time.sleep(1.5)
        print('I clicked on Buttons!')

    def click_on_checkbox_btn(self):
        self.driver.find_element(*self.CHECKBOX_BTN).click()
        # time.sleep(1.5)
        print('I clicked on Checkbox!')

    def click_on_datepicker_btn(self):
        self.driver.find_element(*self.DATEPICKER_BTN).click()
        # time.sleep(1.5)
        print('I clicked on Datepicker!')

    def click_on_drag_and_drop_btn(self):
        self.driver.find_element(*self.DRAG_AND_DROP_BTN).click()
        # time.sleep(1.5)
        print('I clicked on Drag and drop!')

    def click_on_dropdown_btn(self):
        self.driver.find_element(*self.DROPDOWN_BTN).click()
        # time.sleep(1.5)
        print('I clicked on Dropdown!')

    def click_on_enab_disab_elems_btn(self):
        self.driver.find_element(*self.ENAB_DISAB_ELEMS_BTN).click()
        # time.sleep(1.5)
        print('I clicked on Enabled and disabled elements!')

    def click_on_file_upload_btn(self):
        self.driver.find_element(*self.FILE_UPLOAD_BTN).click()
        # time.sleep(1.5)
        print('I clicked on File upload!')

    def click_on_key_mouse_press_btn(self):
        self.driver.find_element(*self.KEY_MOUSE_PRESS_BTN).click()
        # time.sleep(1.5)
        print('I clicked on Key and mouse press!')

    def click_on_modal_btn(self):
        self.driver.find_element(*self.MODAL_BTN).click()
        # time.sleep(1.5)
        print('I clicked on Key and mouse press!')

    def click_on_page_scroll_btn(self):
        self.driver.find_element(*self.PAGE_SCROLL_BTN).click()
        # time.sleep(1.5)
        print('I clicked on Page scroll!')

    def click_on_radio_btn(self):
        self.driver.find_element(*self.RADIO_BTN).click()
        # time.sleep(1.5)
        print('I clicked on Radio button!')

    def click_on_switch_window_btn(self):
        self.driver.find_element(*self.SWITCH_WINDOW_BTN).click()
        # time.sleep(1.5)
        print('I clicked on Switch window!')

    def click_on_complete_web_form_btn(self):
        self.driver.find_element(*self.COMPLETE_WEB_FORM_BTN).click()
        # time.sleep(1.5)
        print('I clicked on Complete web form!')
