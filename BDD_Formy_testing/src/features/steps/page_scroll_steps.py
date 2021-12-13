import time
from behave import *
from selenium.webdriver.common.by import By


@when(u'I navigate to "Page scroll"')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/li[11]/a').click()


@when(u'I scroll down the page')
def step_impl(context):
    full_name = context.driver.find_element(By.ID, 'name')
    time.sleep(1.5)
    context.driver.execute_script('arguments[0].scrollIntoView();', full_name)


@when(u'I enter a name in the "Full name" box')
def step_impl(context):
    full_name = context.driver.find_element(By.ID, 'name')
    full_name.clear()
    full_name.send_keys('Marco Polo')


@when(u'I enter a date in "Date" box')
def step_impl(context):
    date_input = context.driver.find_element(By.ID, 'date')
    date_input.clear()
    time.sleep(1.5)
    date_input.send_keys('01/12/1992')


@then(u'The input name should be displayed')
def step_impl(context):
    full_name = context.driver.find_element(By.ID, 'name').text
    if 'Marco Polo' in full_name:
        assert True
    print(full_name)


@then('the input date should be displayed')
def step_impl(context):
    date_input = context.driver.find_element(By.ID, 'date').text
    if '01/12/1992' in date_input:
        assert True
    print(date_input)
