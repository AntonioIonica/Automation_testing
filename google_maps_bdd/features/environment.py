import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


def after_all(context):
    context.driver.quit()


def before_step(context, step):
    time.sleep(1.5)



