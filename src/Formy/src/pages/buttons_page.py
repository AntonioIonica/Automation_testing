"""
buttons page with hovering and dropdown select
"""

import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class ButtonsPage(BasePage):
    PRIMARY_BTN = (By.XPATH, '/html/body/div/form/div[1]/div/div/button[1]')
    SUCCES_BTN = (By.XPATH, '/html/body/div/form/div[1]/div/div/button[2]')
    INFO_BTN = (By.XPATH, '/html/body/div/form/div[1]/div/div/button[3]')
    WARNING_BTN = (By.XPATH, '/html/body/div/form/div[1]/div/div/button[4]')
    DANGER_BTN = (By.XPATH, '/html/body/div/form/div[1]/div/div/button[5]')
    LINK_BTN = (By.XPATH, '/html/body/div/form/div[1]/div/div/button[6]')
    LEFT_BTN = (By.XPATH, '/html/body/div/form/div[2]/div/div/div/button[1]')
    MIDDLE_BTN = (By.XPATH, '/html/body/div/form/div[2]/div/div/div/button[2]')
    RIGHT_BTN = (By.XPATH, '/html/body/div/form/div[2]/div/div/div/button[3]')
    BTN_1 = (By.XPATH, '/html/body/div/form/div[3]/div/div/div/button[1]')
    BTN_2 = (By.XPATH, '/html/body/div/form/div[3]/div/div/div/button[2]')
    DROPDOWN_BTN = (By.XPATH, '//*[@id="btnGroupDrop1"]')
    DROPDOWN_LINK_1 = (By.XPATH, '/html/body/div/form/div[3]/div/div/div/div/div/a[1]')
    DROPDOWN_LINK_2 = (By.XPATH, '/html/body/div/form/div[3]/div/div/div/div/div/a[2]')

    def hover_on_buttons(self):
        primary_btn = self.driver.find_element(*self.PRIMARY_BTN)
        succes_btn = self.driver.find_element(*self.SUCCES_BTN)
        info_btn = self.driver.find_element(*self.INFO_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(primary_btn).move_to_element(succes_btn).move_to_element(info_btn).perform()

    def click_on_buttons(self):
        self.driver.find_element(*self.WARNING_BTN).click()
        time.sleep(1)
        self.driver.find_element(*self.DANGER_BTN).click()
        time.sleep(1)
        self.driver.find_element(*self.LINK_BTN).click()
        time.sleep(1)
        self.driver.find_element(*self.LEFT_BTN).click()
        time.sleep(1)
        self.driver.find_element(*self.MIDDLE_BTN).click()
        time.sleep(1)
        self.driver.find_element(*self.RIGHT_BTN).click()
        time.sleep(1)
        self.driver.find_element(*self.BTN_1).click()
        time.sleep(1)
        self.driver.find_element(*self.BTN_2).click()
        time.sleep(1)

    def click_on_dropdown(self):
        dropdown_btn = self.driver.find_element(*self.DROPDOWN_BTN)
        dropdown_btn.click()
        time.sleep(1.5)
        dropdown_link_1 = self.driver.find_element(*self.DROPDOWN_LINK_1)
        dropdown_link_1.click()
        time.sleep(3)

