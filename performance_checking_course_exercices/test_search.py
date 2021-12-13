"""
Class: entering the right address will pass the test
and make a report
"""


class TestSearch:
    tst_city = False
    tst_street = False

    def env_setup(self):
        print('This is a environment setup!')
        pass

    def execute_test(self):
        x = input('Please enter an address! ')

        if 'Bucharest' in x:
            self.tst_city = True

        if 'Calea Clujului' in x:
            self.tst_street = True

        # return self.tst_city, self.tst_street
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
    print(test_sch.gen_report())
