"""
Input data parsers
"""
import json


class Utils:

    def get_input_data(self, test_data):
        js_file = open(test_data)
        return json.load(js_file)

    def gen_report(self, my_dict):
        with open('report_file1.json', 'w') as out_file:
            json.dump(my_dict, out_file, indent=4)

    def run_test(self, data, generic_test):
        res = []
        for k, v in data.items():
            status = generic_test(data[k]["input"], data[k]["expected"])
            res.append(dict(input=data[k]["input"],
                            expected=data[k]["expected"],
                            status=status))
        return res

# TODO read-generate report
# TODO rulare
# TODO test_drive = run_test
