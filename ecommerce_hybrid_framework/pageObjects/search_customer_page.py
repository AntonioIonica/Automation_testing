"""
Searching customers by information from the list
"""
from selenium.webdriver.common.by import By


class SearchCustomer:
    TEXT_BOX_EMAIL = (By.ID, 'SearchEmail')
    TEXT_BOX_FNAME = (By.ID, 'SearchFirstName')
    TEXT_BOX_LNAME = (By.ID, 'SearchLastName')
    BTN_SEARCH = (By.ID, 'search-customers')
    TEXT_EMAIL_RESULT = (By.XPATH, '//*[@id="customers-grid"]/tbody/tr/td[2]')
    TEXT_NAME_RESULT = (By.XPATH, '//*[@id="customers-grid"]/tbody/tr/td[3]')

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(*self.TEXT_BOX_EMAIL).clear()
        self.driver.find_element(*self.TEXT_BOX_EMAIL).send_keys(email)

    def set_fname(self, fname):
        self.driver.find_element(*self.TEXT_BOX_FNAME).clear()
        self.driver.find_element(*self.TEXT_BOX_FNAME).send_keys(fname)

    def set_lname(self, lname):
        self.driver.find_element(*self.TEXT_BOX_LNAME).clear()
        self.driver.find_element(*self.TEXT_BOX_LNAME).send_keys(lname)

    def click_search_btn(self):
        self.driver.find_element(*self.BTN_SEARCH).click()

    def search_customers_by_email(self, email):
        result = False
        email_result = self.driver.find_element(*self.TEXT_EMAIL_RESULT).text
        if email == email_result:
            result = True
        return result

    def search_customers_by_name(self, name):
        result = False
        name_result = self.driver.find_element(*self.TEXT_NAME_RESULT).text
        if name == name_result:
            result = True
        return result
