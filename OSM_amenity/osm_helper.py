"""
Getting the coordinates from the amenity name
and using the first coordinates into the map
"""

import json


class osmHelper:

    def write_json(self, response, file_name='amenities_data.json'):
        """
        :param response: OSM json raw response
        :param file_name: name of file
        """
        with open(file_name, mode='w') as file_json:
            json.dump(response, file_json)

    def process_websites(self, response):
        websites = []
        coordinates = []
        for x in response['elements']:
            if 'website' in x['tags']:
                websites.append(x['tags']['website'])
                coordinates.append(str(x['lat']) + ',' + str(x['lon']))
        self.write_json(websites, 'website_list.json')
        return coordinates
