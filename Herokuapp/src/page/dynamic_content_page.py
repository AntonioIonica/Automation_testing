"""
Dynamic content
"""

from Herokuapp.src.page.base_page import BasePage


class DynamicContent(BasePage):

    def refresh_page(self):
        self.driver.refresh()