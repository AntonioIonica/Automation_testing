"""
Broken image
2 of the total of 3 are broken
"""

import requests
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class BrokenImage(BasePage):

    def broken_images(self):
        image_list = self.driver.find_elements(By.TAG_NAME, 'img')
        print('Total number of images are ' + str(len(image_list)))
        broken_img = 0
        for img in image_list:
            response = requests.get(img.get_attribute('src'), stream=True)
            if response.status_code != 200:
                print(img.get_attribute('outerHTML') + " is broken.")
                broken_img = (broken_img + 1)
        print('The page has ' + str(broken_img) + ' broken images')
