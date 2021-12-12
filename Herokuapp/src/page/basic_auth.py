"""
Basic authentification with browser type login
user: admin
password: admin
"""

from Herokuapp.src.page.base_page import BasePage


class BasicAuth(BasePage):

    def basic_auth(self):
        usr = 'admin'
        pwd = 'admin'
        self.driver.get('https://' + usr + ':' + pwd + '@' + 'the-internet.herokuapp.com/basic_auth')
