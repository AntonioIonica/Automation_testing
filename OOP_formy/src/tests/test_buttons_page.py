"""
Testing the clicked buttons if they are selected
"""

import time
import unittest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.buttons_page import ButtonsPage
from selenium import webdriver


class TestButtonsPage(unittest.TestCase):
    BUTTONS_BTN = (By.CSS_SELECTOR, 'body > div > div > li:nth-child(6) > a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://formy-project.herokuapp.com/')
        time.sleep(2)
        self.driver.maximize_window()
        self.driver.find_element(*self.BUTTONS_BTN).click()

    def test_hover_on_buttons(self):
        buttons = ButtonsPage(self.driver)
        buttons.hover_on_buttons()
        success_btn = self.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div/div/button[2]')
        self.assertFalse(success_btn.is_selected())
        time.sleep(1.5)
        self.driver.close()

    def test_click_on_buttons(self):
        buttons = ButtonsPage(self.driver)
        buttons.click_on_buttons()
        btn_2 = self.driver.find_element(By.XPATH, '/html/body/div/form/div[3]/div/div/div/button[1]')
        self.assertTrue(btn_2.is_selected())
        time.sleep(1.5)
        self.driver.close()

    def test_click_on_dropdown(self):
        buttons = ButtonsPage(self.driver)
        buttons.click_on_dropdown()
        dropdown_show = self.driver.find_element(By.XPATH, '/html/body/div/form/div[3]/div/div/div/div/div')
        self.assertFalse(dropdown_show.is_displayed())
        time.sleep(1.5)
        self.driver.close()

    def tearDown(self) -> None:
        time.sleep(1.5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
