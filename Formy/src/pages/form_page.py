"""
form page
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage


class FormPage(BasePage):
    HEADER = (By.CSS_SELECTOR, 'body > div > h1')
    F_NAME = (By.ID, 'first-name')
    L_NAME = (By.ID, 'last-name')
    JOB_TITLE = (By.ID, 'job-title')
    RADIO_BUTTON_1 = (By.ID, 'radio-button-1')
    RADIO_BUTTON_3 = (By.ID, 'radio-button-3')
    SEX_BUTTON_MALE = (By.ID, 'checkbox-1')
    SELECT_MENU = (By.ID, 'select-menu')
    EXPERIENCE_0 = (By.CSS_SELECTOR, '#select-menu > option:nth-child(2)')
    DATE_PICKER = (By.ID, 'datepicker')
    SUBMIT_BTN = (By.CSS_SELECTOR, 'body > div > form > div > div:nth-child(15) > a')

    def click_on_f_name(self):
        self.driver.find_element(*self.F_NAME).send_keys('John')

    def click_on_l_name(self):
        self.driver.find_element(*self.L_NAME).send_keys('Snow')

    def click_on_job_title(self):
        self.driver.find_element(*self.JOB_TITLE).send_keys('Engineer')

    def click_on_education_junior(self):
        button1 = self.driver.find_element(*self.RADIO_BUTTON_1)
        button_state = button1.is_selected()
        print(f'HighSchool button state is {button_state}')
        time.sleep(1.5)
        button1.click()
        button_state = button1.is_selected()
        print(f'HighSchool button state is {button_state}')
        time.sleep(1.5)
        button3 = self.driver.find_element(*self.RADIO_BUTTON_3)
        button3.click()
        button3_state = button3.is_selected()
        print(f'GradSchool button state is {button3_state}')

    def click_on_sexual_identification(self):
        self.driver.find_element(*self.SEX_BUTTON_MALE).click()

    def click_on_experience(self):
        element = self.driver.find_element(*self.SELECT_MENU)
        drp = Select(element)
        drp.select_by_index(1)
        all_options = drp.options[1:]
        for option in all_options:
            print(option.text)

    def enter_date(self):
        time.sleep(1.5)
        date_picker = self.driver.find_element(*self.DATE_PICKER)
        date_picker.clear()
        time.sleep(1.5)
        date_picker.send_keys('07/18/1996')
        time.sleep(2)

    def click_on_submit(self):
        self.driver.find_element(*self.SUBMIT_BTN).click()

    def header_name(self):
        header = self.driver.find_element(*self.HEADER).text
        if 'Complete Web Form' in header:
            print('Header name is correct!')
            return True
        else:
            return False
