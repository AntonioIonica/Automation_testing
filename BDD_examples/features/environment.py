from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


def after_all(context):
    context.driver.quit()


def after_scenario(context, scenario):
    context.driver.quit()
