from pageObjects.admin_login_page import AdminLoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LoginGeneration
from pageObjects.search_customer_page import SearchCustomer
from pageObjects.add_customer_page import AddCustomer


class TestSearchCustomerByName:
    URL = ReadConfig.get_url()
    email_info = ReadConfig.get_admin_email()
    pwd_info = ReadConfig.get_admin_pwd()

    logger = LoginGeneration.loggen()

    def test_search_customer_by_name(self, setUp):
        self.logger.info('***Test Admin Customers Page***')
        self.logger.info('***Searching customer by email***')
        self.driver = setUp
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        self.login = AdminLoginPage(self.driver)
        self.login.set_email(self.email_info)
        self.login.set_pwd(self.pwd_info)
        self.login.click_login()
        self.logger.info('*** Login successful ***')

        self.logger.info('***Searching customer by name***')
        self.addcustomer = AddCustomer(self.driver)
        self.addcustomer.click_on_customers_navi()
        self.addcustomer.click_on_customers_menu()

        search_customer = SearchCustomer(self.driver)
        search_customer.set_fname('Victoria')
        search_customer.set_lname('Terces')
        search_customer.click_search_btn()
        self.driver.implicitly_wait(3)
        status = search_customer.search_customers_by_name('Victoria Terces')
        assert status == True
        self.logger.info('*** test_search_customer_by_email test finished ***')
        self.driver.close()