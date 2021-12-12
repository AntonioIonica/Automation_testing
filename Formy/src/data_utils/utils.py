"""
Data send keys from Json file
"""

import json

class Utils:

    @staticmethod
    def get_data():
        js_file = open('/keys_data/input_data.json', 'r')
        return json.load(js_file)

    @staticmethod
    def get_keys(data):