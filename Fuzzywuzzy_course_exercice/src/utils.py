"""
Input data parsers
Where the given json file as attribute is open, then is dumped in another json file after comparing the data in it
"""
import json


class Utils:

    @staticmethod
    def get_input_data(test_data):
        js_file = open(test_data)
        return json.load(js_file)

    @staticmethod
    def gen_report(my_dict):
        with open('report_file1.json', 'w') as out_file:
            json.dump(my_dict, out_file, indent=4)

    @staticmethod
    def run_test(data, generic_test):
        res = []
        for k, v in data.items():
            status = generic_test(data[k]["input"], data[k]["expected"])
            res.append(dict(input=data[k]["input"],
                            expected=data[k]["expected"],
                            status=status))
        return res


