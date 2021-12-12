"""
Main execution
"""
from Curs_9.src.test_script import test_case2
from Curs_9.src.utils import Utils

if __name__ == '__main__':
    utils_data = Utils()
    datas = utils_data.get_input_data(
        'C:/Users/anton/PycharmProjects/Automation_testing/src/Curs_9/test_data/input_data.json')
    output = utils_data.run_test(datas, test_case2)
    print(output)
    utils_data.gen_report(output)
