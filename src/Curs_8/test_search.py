"""
Test class
"""
from src.Curs_8.recap_ABC import TestModel


class TestSearch(TestModel):
    tst_city = False
    tst_street = False

    def env_setup(self):
        print('This is a environment setup!')
        pass

    def execute_test(self):
        x = input('Please enter an adress! ')
        if 'Bucharest' in x:
            self.tst_city = True
        if 'Calea Clujului' in x:
            self.tst_street = True
        #return self.tst_city, self.tst_street
        print(self.tst_city)
        print(self.tst_street)

    def close(self):
        pass

    @staticmethod
    def gen_report():
        return {'name': 'Gelu', 'age': 46,
                'Test_name': TestSearch.tst_street}

if __name__ == '__main__':
    test_sch = TestSearch()
    test_main = TestModel()
    print(test_sch.gen_report())
    print(test_main.gen_report())

    #test_result = test_sch.execute_test()
    #print(test_result)
