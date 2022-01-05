"""
OSM coordinates where you specific the exact amenity
"""
import requests


class osmApi:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def get_nodes(self, amenity):
        """
        :param amenity: giving different amenities from a city
        :return: by giving different amenities, the websites and other info changes and is writen in dublin_pub.json file
        """
        url = 'https://overpass.kumi.systems/api/interpreter'
        query = f"[out:json]; node[amenity='{amenity}']({self.coordinates[0]},{self.coordinates[1]},{self.coordinates[2]},{self.coordinates[3]}); out;"
        response = requests.get(url, params={'data': query})
        return response.json()
