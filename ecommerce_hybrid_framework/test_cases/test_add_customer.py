from selenium.webdriver.common.by import By

from pageObjects.admin_login_page import AdminLoginPage
from pageObjects.add_customer_page import AddCustomer
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LoginGeneration
import string
import random


class TestAddCustomer:
    URL = ReadConfig.get_url()
    email_info = ReadConfig.get_admin_email()
    pwd_info = ReadConfig.get_admin_pwd()

    logger = LoginGeneration.loggen()

    def test_add_customer(self, setUp):
        self.logger.info("*** Test Adding a Customer testcase***")
        self.driver = setUp
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        self.login = AdminLoginPage(self.driver)
        self.login.set_email(self.email_info)
        self.login.set_pwd(self.pwd_info)
        self.login.click_login()
        self.logger.info("*** Login successful ***")

        self.addcustomer = AddCustomer(self.driver)
        self.addcustomer.click_on_customers_navi()
        self.addcustomer.click_on_customers_menu()
        self.addcustomer.click_to_add_new_customer()

        self.logger.info("*** Adding new customer ***")
        self.email = random_generator() + '@gmail.com'
        self.addcustomer.set_customer_email(self.email)
        self.addcustomer.set_customer_pwd('dawdadaw')
        self.addcustomer.set_customer_fname('Andew')
        self.addcustomer.set_customer_lname('John')
        self.addcustomer.set_gender_male()
        self.addcustomer.set_birtday()
        self.addcustomer.set_company('SRL Monday')

        self.logger.info("*** Saving info ***")
        self.addcustomer.click_on_save()

        self.message = self.driver.find_element(By.TAG_NAME, 'body').text
        if 'customer has been added successfully.' in self.message:
            assert True
            self.logger.info("*** Customer added successfully ***")
        else:
            self.driver.save_screenshot('.\\screenshots\\' + 'test_add_customer.pgn')
            self.logger.info("*** Add customer test failed ***")
            assert False

        self.driver.close()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
