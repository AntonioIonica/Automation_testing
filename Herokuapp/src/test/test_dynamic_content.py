"""
Testing dynamic text and images
"""

import time, unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from Herokuapp.src.page.dynamic_content_page import DynamicContent

service = Service('/chromedriver.exe')


class TestDynamicContent(unittest.TestCase):
    NAVI = (By.XPATH, '//*[@id="content"]/ul/li[12]/a')
    TEXT_1 = (By.XPATH, '//*[@id="content"]/div[1]/div[2]')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.find_element(*self.NAVI).click()
        self.driver.implicitly_wait(5)

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    def test_dynamic_text(self):
        text_1 = self.driver.find_element(*self.TEXT_1).text
        if 'Dolorum nesciunt inventore quod autem odio magni minus autem tenetur temporibus' \
           ' quibusdam labore est molestiae dolore consequatur explicabo unde quia' \
           ' perferendis id nam quas earum sint ex non quae quo veritatis natus omnis laudantium.' != text_1:
            assert True
        else:
            assert False
        dynamic = DynamicContent(self.driver)
        dynamic.refresh_page()
        if 'Dolorum nesciunt inventore quod autem odio magni minus autem tenetur temporibus' \
           ' quibusdam labore est molestiae dolore consequatur explicabo unde quia' \
           ' perferendis id nam quas earum sint ex non quae quo veritatis natus omnis laudantium.' != text_1:
            assert True
        else:
            assert False
