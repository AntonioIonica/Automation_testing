"""
TestSuite run
"""

import unittest
import HtmlTestRunner
import os
from tests import test_autocomplete_page, test_form_page, test_home_page,\
    test_switch_window_page, test_page_scroll, test_drag_drop, test_buttons_page, test_file_upload, test_enab_disab

direct = os.getcwd()

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_autocomplete_page.TestAutocomplete),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_form_page.TestFormPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_home_page.TestHomePage),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_switch_window_page.TestSwitchWindow),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_page_scroll.TestPageScroll),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_drag_drop.TestDragDrop),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_buttons_page.TestButtonsPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_file_upload.TestFileUpload),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_enab_disab.TestEnabledDisabledEle)
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