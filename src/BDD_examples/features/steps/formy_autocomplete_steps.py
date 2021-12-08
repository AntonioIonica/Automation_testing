from behave import *
from selenium.webdriver.common.by import By


@given(u'I clicked on autocomplete button')
def step_impl(context):
    context.driver.get('https://formy-project.herokuapp.com/')
    context.driver.maximize_window()
    context.driver.implicitly_wait(2)
    context.driver.find_element(By.XPATH, '/html/body/div/div/li[1]/a').click()
    context.driver.implicitly_wait(2)

@when(u'I type cl in address field')
def step_impl(context):
    context.driver.find_element(By.ID, 'autocomplete').send_keys('cl')

@then(u'Cluj should be visible')
def step_impl(context):
    failed_geo = context.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/span').text
    if 'This page can\'t load' == failed_geo:
        assert False, 'Test Failed'

# TODO google maps with scenario outline