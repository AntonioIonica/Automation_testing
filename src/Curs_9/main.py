"""
Main execution
"""
from src.Curs_9.src.test_script import test_case1
from src.Curs_9.src.utils import Utils


if __name__ == '__main__':
    # data = get_input_data('C:/Users/anton/PycharmProjects/Automation_testing/src/Curs_9/test_data/input_data.json')
    # print(data)
    # output = run_test(data, test_case1)
    # print(output)
    # gen_report(output)

    utils_data = Utils()
    datas = utils_data.get_input_data('C:/Users/anton/PycharmProjects/Automation_testing/'
                                            'src/Curs_9/test_data/input_data.json')
    output = utils_data.run_test(datas, test_case1)
    print(output)
    utils_data.gen_report(output)

