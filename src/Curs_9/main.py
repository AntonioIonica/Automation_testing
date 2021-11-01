"""
Main execution
"""
from src.Curs_9.src.utils import Utils
from src.Curs_9.src.test_script import TestCases



if __name__ == '__main__':
    # data = get_input_data('C:/Users/anton/PycharmProjects/Automation_testing/src/Curs_9/test_data/input_data.json')
    # print(data)
    # output = run_test(data, test_case1)
    # print(output)
    # gen_report(output)

    utils_data = Utils()
    datas = utils_data.get_input_data('C:/Users/anton/PycharmProjects/Automation_testing/'
                                            'src/Curs_9/test_data/input_data.json')
    cases = TestCases()
    case_1 = cases.test_case1()
    case_2 = cases.test_case2()
    output_1 = utils_data.run_test(datas, case_1)
    output_2 = utils_data.run_test(datas, case_2)

