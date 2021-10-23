"""
Main
"""
from src.Curs_8.test_performance import TestPerf
from src.Curs_8.test_search import TestSearch

test_sch = TestSearch()
test_perf = TestPerf()

for test in test_sch, test_perf:
    test.execute_test()

#test_result = test_sch.execute_test()
#print(test_result)

#test_perf.execute_test()
