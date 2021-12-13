"""
Generating a report from all the testcases using TestSuite
Smoketest form
the report form is html using HTMLTestRunner
"""
import unittest
import HtmlTestRunner
import login_site
import test_auth
import test_context_menu


class TestReport(unittest.TestCase):
    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_auth.TestAuth),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_site.TestLogin),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_context_menu.TestContext)
        ])

        test_runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Report',
            report_name='Smoke Test'
        )

        test_runner.run(smoke_test)


if __name__ == '__main__':
    unittest.main()
