"""
Multiple search will be a child of Test_search
"""
from test_performance import TestPerf
from test_search import TestSearch


class FuzzySearch(TestSearch):

    @staticmethod
    def gen_report():
        return {'name': 'Andrei', 'age': 13}


if __name__ == '__main__':
    test_perf = TestPerf()
    test_perf.execute_test()
    test_sch = TestSearch()
    print(test_sch.gen_report())
    fuzzy_sch = FuzzySearch()
    print(fuzzy_sch.gen_report())
