import time
from behave import *
from selenium.webdriver.common.by import By


@when(u'I navigate to File upload')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/li[8]/a').click()


@when(u'I click on Choose button and upload a picture')
def step_impl(context):
    text_box = context.driver.find_element(By.ID, 'file-upload-field')
    text_box.send_keys('C:/Users/anton/PycharmProjects/Automation_testing/exercices_todo/blue.png')
    time.sleep(1.5)


@then(u'The box should had the name of the picture')
def step_impl(context):
    text_box = context.driver.find_element(By.ID, 'file-upload-field').text
    if 'blue.png' in text_box:
        assert True


@when(u'I click on Choose a file button and upload a picture')
def step_impl(context):
    text_box = context.driver.find_element(By.ID, 'file-upload-field')
    text_box.send_keys('C:/Users/anton/PycharmProjects/Automation_testing/exercices_todo/blue.png')
    time.sleep(1.5)


@when(u'I press reset')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/form/div/div/span[2]').click()
    time.sleep(1.5)


@then(u'The box should be reset')
def step_impl(context):
    text_box = context.driver.find_element(By.ID, 'file-upload-field').text
    if 'blue.png' not in text_box:
        assert True
