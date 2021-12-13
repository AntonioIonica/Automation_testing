"""
Main script execution
Where the data is selected (json)
The data is compared and the output (report) is generated
"""
from Fuzzywuzzy_course_exercice.src.test_script import test_case2
from Fuzzywuzzy_course_exercice.src.utils import Utils

if __name__ == '__main__':
    utils_data = Utils()
    datas = utils_data.get_input_data(
        'C:/Users/anton/PycharmProjects/Automation_testing/src/Fuzzywuzzy_course_exercice/test_data/input_data.json')
    output = utils_data.run_test(datas, test_case2)
    print(output)
    utils_data.gen_report(output)
