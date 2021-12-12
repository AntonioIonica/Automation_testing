"""
Main
"""
from test_performance import TestPerf
from test_search import TestSearch

test_sch = TestSearch()
test_perf = TestPerf()

for test in test_sch, test_perf:
    test.execute_test()

