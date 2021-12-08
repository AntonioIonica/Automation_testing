from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    print('Welcome!')
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


def after_all(context):
    print('Good bye!')
    context.driver.quit()


def before_scenario(context, scenario):
    print('New Scenario')

# TODO de facut before step