"""
autocomplete page
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AutocompletePage(BasePage):
    ADR = (By.ID, 'autocomplete')
    STR_1 = (By.ID, 'street_number')
    STR_2 = (By.ID, 'route')
    CITY = (By.ID, 'locality')
    STATE = (By.ID, 'administrative_area_level_1')
    ZIP = (By.ID, 'postal_code')
    COUNTRY = (By.ID, 'country')

    def enter_adr(self):
        """

        :return:
        """
        print('Adress entered!')
        self.driver.find_element(*self.ADR).send_keys('Bucharest')

    def enter_str_1(self):
        print('Street 1 entered!')
        self.driver.find_element(*self.STR_1).send_keys('Calea Victoriei')

    def enter_str_2(self):
        print('Street 2 entered!')
        self.driver.find_element(*self.STR_2).send_keys('Victoriei')

    def enter_city(self):
        print('City entered!')
        self.driver.find_element(*self.CITY).send_keys('Bucharest')

    def enter_state(self):
        print('State entered!')
        self.driver.find_element(*self.STATE).send_keys('Romania')

    def enter_zip(self):
        print('ZIP-Code entered!')
        self.driver.find_element(*self.ZIP).send_keys('077186')

    def enter_country(self):
        print('Country entered!')
        self.driver.find_element(*self.COUNTRY).send_keys('Romania')

    def title_page(self):
        print('Title verified!')
        return self.driver.title
