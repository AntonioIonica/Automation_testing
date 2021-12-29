"""
get openstreetmap amenities using API call
giving amenity, there is a report writen and also the website of specified amenity is given in console
"""
import json, time
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def call_osm_api(amenity):
    """
    :param amenity: giving different amenities from a city
    :return: by giving different amenities, the websites and other info changes and is writen in dublin_pub.json file
    """
    url = 'https://overpass.kumi.systems/api/interpreter'
    query = '[out:json]; node[amenity=' + amenity + '](53.2987342,-6.3870259,53.4105416,-6.1148829); out;'
    response = requests.get(url, params={'data': query})
    return response.json()


# TODO sa adaugam si alte orase(coordonate) pentru amenity

# query = """
# [out:json];
# node
#   [amenity=pub]
#   (53.2987342,-6.3870259,53.4105416,-6.1148829);
# out;
# """
#
# response = requests.get(url, params={'data': query})
#
# data_output = response.json()
data_output = call_osm_api('dentist')

with open('dublin_pub.json', mode='w') as file_json:
    json.dump(data_output, file_json)

websites = []
coordinates = []
for x in data_output['elements']:
    if 'website' in x['tags']:
        print(x['tags']['website'])
        websites.append(x['tags']['website'])
        coordinates.append(str(x['lat']) + ',' + str(x['lon']))
    else:
        print('Website not available')
with open('websites.json', mode='w') as website_json:
    json.dump(websites, website_json)
print(coordinates)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.openstreetmap.org/')
driver.maximize_window()
driver.implicitly_wait(3)

driver.find_element(By.CSS_SELECTOR, '#sidebar #query').send_keys(coordinates[0])
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,
                    '#sidebar > div.search_forms > form.search_form.px-1.py-2 > div > div.col > div > div.input-group-append > input').click()
time.sleep(5)


# TODO migrate the current script in a class, modeled by unittest.TestCases
