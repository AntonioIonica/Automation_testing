from selenium import webdriver
import unittest, time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestClass(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.google.com/')
        self.driver.maximize_window()
        self.driver.find_element(By.ID, 'L2AGLb').click()
        google_maps = self.driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        google_maps.send_keys('Google maps')
        google_maps.submit()
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/h3').click()
        time.sleep(15)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_down(self):
        print('caca')


if __name__ == '__main__':
    unittest.main()
