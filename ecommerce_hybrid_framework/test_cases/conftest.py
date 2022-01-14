from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def setUp():
    """
    :return: driver for Chrome
    """
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver
