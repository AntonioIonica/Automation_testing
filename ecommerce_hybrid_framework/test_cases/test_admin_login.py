"""
Testing and asserting the objects
"""
from pageObjects.admin_login_page import AdminLoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LoginGeneration


class TestAdminLoginPage:
    URL = ReadConfig.get_url()
    email_info = ReadConfig.get_admin_email()
    pwd_info = ReadConfig.get_admin_pwd()

    logger = LoginGeneration.loggen()

    def test_page_title(self, setUp):
        self.logger.info('***Test Admin Login Page***')
        self.logger.info('***Home page title verifier***')
        self.driver = setUp
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        actual_title = self.driver.title
        if actual_title == 'Your store. Login':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot('.\\screenshots\\' + 'test_page_title.png')
            assert False
            self.driver.close()
            self.logger.info('***Home page title verifier failed***')

    def test_admin_login(self, setUp):
        self.logger.info('***Admin login started***')
        self.driver = setUp
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.login = AdminLoginPage(self.driver)
        self.login.set_email(self.email_info)
        self.login.set_pwd(self.pwd_info)
        self.login.click_login()
        page_title = self.driver.title
        if page_title == 'Dashboard / nopCommerce administration':
            assert True
            self.login.click_logout()
            self.driver.close()
            self.logger.info('***Login passed***')
        else:
            self.driver.save_screenshot('.\\screenshots\\' + 'test_admin_login.png')
            assert False
            self.driver.close()
            self.logger.info('***Login failed***')
