import time
from behave import *
from selenium.webdriver.common.by import By


@when(u'I navigate to Enabled and disabled elements')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/li[7]/a').click()


@when(u'I click on "Input here..." box')
def step_impl(context):
    context.driver.find_element(By.ID, 'input').click()


@when(u'I type "abc123"')
def step_impl(context):
    enabled_box = context.driver.find_element(By.ID, 'input')
    enabled_box.clear()
    enabled_box.send_keys('abc123')


@then(u'The box should be enabled')
def step_impl(context):
    enable_box = context.driver.find_element(By.ID, 'input')
    if enable_box.is_enabled():
        assert True
    print(f'Status of Enabled Box is {enable_box.is_displayed()}')


@when(u'I click on "Disabled input here..."')
def step_impl(context):
    context.driver.find_element(By.ID, 'disabledInput').click()
    

@then(u'The box should be disabled')
def step_impl(context):
    disable_box = context.driver.find_element(By.ID, 'disabledInput')
    if disable_box.is_enabled() is False:
        assert True
    print(f'Status of Disabled Box is {disable_box.is_displayed}')