from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    print('Welcome')


def after_all(context):
    print('Good bye!')


def after_scenario(context, scenario):
    context.driver.quit()
