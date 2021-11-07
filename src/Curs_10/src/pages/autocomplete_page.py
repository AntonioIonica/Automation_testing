"""
autocomplete page
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AutocompletePage(BasePage):

    ADR = 'autocomplete'
    STR_1 = 'street_number'
    STR_2 = 'route'
    CITY = 'locality'
    STATE = 'administrative_area_level_1'
    ZIP = 'postal_code'
    COUNTRY = 'country'

    def enter_adr(self):
        print('Adress entered!')
        self.driver.find_element(By.ID, self.ADR).send_keys('Bucharest')

    def enter_str_1(self):
        print('Street 1 entered!')
        self.driver.find_element(By.ID, self.STR_1).send_keys('Calea Victoriei')

    def enter_str_2(self):
        print('Street 2 entered!')
        self.driver.find_element(By.ID, self.STR_2).send_keys('Victoriei')

    def enter_city(self):
        print('City entered!')
        self.driver.find_element(By.ID, self.CITY).send_keys('Bucharest')

    def enter_state(self):
        print('State entered!')
        self.driver.find_element(By.ID, self.STATE).send_keys('Bucharest')

    def enter_zip(self):
        print('ZIP-Code entered!')
        self.driver.find_element(By.ID, self.ZIP).send_keys('077186')

    def enter_country(self):
        print('Country entered!')
        self.driver.find_element(By.ID, self.COUNTRY).send_keys('Romania')

    def title_page(self):
        print('Title verified!')
        return self.driver.title

