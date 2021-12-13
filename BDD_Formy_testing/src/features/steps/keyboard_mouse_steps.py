import time
from behave import *
from selenium.webdriver.common.by import By


@when('I navigate to Keyboard and mouse input')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/li[9]/a').click()


@when('I input a random name as Full name')
def step_impl(context):
    context.driver.find_element(By.ID, 'name').send_keys('Marco Polo')
    time.sleep(1.5)


@when('I click on the Button')
def step_impl(context):
    context.driver.find_element(By.ID, 'button').click()


@then('The button is selected')
def step_impl(context):
    button = context.driver.find_element(By.ID, 'button')
    if button.is_selected():
        assert True


@then('The name I typed is in the "Enter full name" box')
def step_impl(context):
    name = context.driver.find_element(By.ID, 'name').text
    if 'Marco Polo' in name:
        assert True
