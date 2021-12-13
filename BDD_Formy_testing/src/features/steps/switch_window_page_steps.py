import time
from behave import *
from selenium.webdriver.common.by import By


@when(u'I navigate to "Switch window" page')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/li[13]/a').click()


@when(u'I click on "Open new tab" button')
def step_impl(context):
    context.driver.find_element(By.ID, 'new-tab-button').click()


@then(u'A new window will open')
def step_impl(context):
    handles = context.driver.window_handles
    for handle in handles:
        context.driver.switch_to.window(handle)
    context.driver.switch_to.window(handles[0])


@when(u'I click on "Open alert" button')
def step_impl(context):
    context.driver.find_element(By.ID, 'alert-button').click()


@when(u'An alert will pop up and I click on ok')
def step_impl(context):
    context.driver.switch_to.alert.accept()


@then('The alert will close')
def step_impl(context):
    try:
        click_alert = context.driver.switch_to_alert()
        click_alert.accept()
    except:
        assert True
