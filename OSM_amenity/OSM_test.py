import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from OSM_amenity.osm_helper import osmHelper
from OSM_amenity.osm_api import osmApi


class osmTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.openstreetmap.org/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_osm_coordinates(self):
        api = osmApi(53.2987342, -6.3870259, 53.4105416, -6.1148829)
        dentist_nodes = api.get_nodes('dentist')
        helper = osmHelper()
        helper.write_json(dentist_nodes)
        dentist_coords = helper.process_websites(dentist_nodes)

        self.driver.find_element(By.CSS_SELECTOR, '#sidebar #query').send_keys(dentist_coords[0])
        self.driver.find_element(By.CSS_SELECTOR,
                                 '#sidebar > div.search_forms > form.search_form.px-1.py-2 > div > div.col > div > div.input-group-append > input').click()
        self.driver.implicitly_wait(5)
        area_checker = self.driver.find_element(By.XPATH, '//*[@id="sidebar_content"]/div[3]').text
        self.assertEqual(area_checker, 'Leinster, Ireland')


if __name__ == '__main__':
    unittest.main()
