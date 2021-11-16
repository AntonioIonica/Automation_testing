"""
TestSuite run
"""

import unittest
import HtmlTestRunner
import os
from tests import test_autocomplete_page, test_form_page, test_home_page

direct = os.getcwd()

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_autocomplete_page.TestAutocomplete),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_form_page.TestFormPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_home_page.TestHomePage)
        ])

        outfile = open(direct + 'SmokeTest.html', 'w')

        runner1 = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            stream=outfile,
            report_title='Test Report',
            report_name='Smoke Tests'
        )

        runner1.run(smoke_test)

if __name__ == '__main__':
    unittest.main()