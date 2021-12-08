from selenium import webdriver
import unittest, time
from webdriver_manager.chrome import ChromeDriverManager

class TestClass(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.google.com/maps')
        time.sleep(15)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_down(self):
        print('caca')

if __name__ == '__main__':
    unittest.main()