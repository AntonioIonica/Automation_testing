"""
Dynamic content
"""

from OOP_the_internet_herokuapp.src.page.base_page import BasePage


class DynamicContent(BasePage):

    def refresh_page(self):
        self.driver.refresh()