from selenium.webdriver.common.by import By


class AddCustomer:
    NAVI_CUSTOMERS_MENU = (By.XPATH, '/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p')
    NAVI_CUSTOMERS = (By.XPATH, '/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p')
    BTN_ADD_CUSTOMER = (By.XPATH, '/html/body/div[3]/div[1]/form[1]/div/div/a')

    TEXT_BOX_EMAIL = (By.ID, 'Email')
    TEXT_BOX_PWD = (By.ID, 'Password')
    TEXT_BOX_FNAME = (By.ID, 'FirstName')
    TEXT_BOX_LNAME = (By.ID, 'LastName')
    CHECKBOX_GENDER_MALE = (By.ID, 'Gender_Male')
    BIRTH_DATE = (By.ID, 'DateOfBirth')
    TEXT_BOX_COMPANY = (By.ID, 'Company')
    RADIOBOX_TAX = (By.ID, 'IsTaxExempt')
    DROPDOWN_VENDOR = (By.ID, 'VendorId')
    ACTIVE_ACCOUNT = (By.ID, 'Active')
    TEXT_BOX_ADMIN_COMMENT = (By.ID, '//*[@id="AdminComment"]')
    BTN_SAVE = (By.XPATH, '/html/body/div[3]/div[1]/form/div[1]/div/button[1]')

    def __init__(self, driver):
        self.driver = driver

    def click_on_customers_navi(self):
        self.driver.find_element(*self.NAVI_CUSTOMERS_MENU).click()

    def click_on_customers_menu(self):
        self.driver.find_element(*self.NAVI_CUSTOMERS).click()

    def click_to_add_new_customer(self):
        self.driver.find_element(*self.BTN_ADD_CUSTOMER).click()

    def set_customer_email(self, email):
        self.driver.find_element(*self.TEXT_BOX_EMAIL).send_keys(email)

    def set_customer_pwd(self, pwd):
        self.driver.find_element(*self.TEXT_BOX_PWD).send_keys(pwd)

    def set_customer_fname(self, fname):
        self.driver.find_element(*self.TEXT_BOX_FNAME).send_keys(fname)

    def set_customer_lname(self, lname):
        self.driver.find_element(*self.TEXT_BOX_LNAME).send_keys(lname)

    def set_gender_male(self):
        self.driver.find_element(*self.CHECKBOX_GENDER_MALE).click()

    def set_birtday(self):
        self.driver.find_element(*self.BIRTH_DATE).clear()
        self.driver.find_element(*self.BIRTH_DATE).send_keys('01/07/1996')

    def set_company(self, company):
        self.driver.find_element(*self.TEXT_BOX_COMPANY).send_keys(company)

    def click_on_save(self):
        self.driver.find_element(*self.BTN_SAVE).click()
