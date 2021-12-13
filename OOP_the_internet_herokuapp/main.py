"""
TestSuite run
"""

import unittest
import HtmlTestRunner
import os

from src.test import test_add_remove_elems_page, test_basic_auth, test_broken_image_page, test_checkboxes_page, \
    test_context_menu, test_dropdown, test_dynamic_content, test_form_auth, test_home_page

direct = os.getcwd()


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_add_remove_elems_page.TestAddRemove),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_basic_auth.TestBasicAuth),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_broken_image_page.TestBrokenImage),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_checkboxes_page.TestCheckboxes),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_context_menu.TestContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_dropdown.TestDropdown),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_dynamic_content.TestDynamicContent),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_form_auth.TestFormAuth),
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
