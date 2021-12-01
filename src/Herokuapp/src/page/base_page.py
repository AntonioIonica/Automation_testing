"""
Driver with implicitly wait: 30 seconds
"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
