"""
Setting the webdriver for Chrome and installing the most recent update everytime
"""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


def before_scenario(context, scenario):
    print('New testing scenario')


def before_step(context, step):
    """
    Setting a time sleep for educational purpose
    :param context:
    :param step:
    :return: None
    """
    time.sleep(1)


def after_all(context):
    """
    Closing the driver
    :param context:
    :return:
    """
    context.driver.quit()


def after_scenario(context, scenario):
    print('Testing scenario run!')
