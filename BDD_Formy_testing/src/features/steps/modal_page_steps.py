import time
from behave import *
from selenium.webdriver.common.by import By


@when(u'I navigate to modal page')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/li[10]/a').click()
    time.sleep(1.5)


@when(u'I click on "Open Modal"')
def step_impl(context):
    context.driver.find_element(By.ID, 'modal-button').click()
    time.sleep(1.5)


@when(u'I click on ok button')
def step_impl(context):
    context.driver.find_element(By.ID, 'ok-button').click()


@then(u'The modal window closes')
def step_impl(context):
    modal_title = context.driver.find_element(By.XPATH, '//*[@id="exampleModal"]/div/div')
    if modal_title.is_displayed() is False:
        assert True
    else:
        assert False


@when(u'I click on close button')
def step_impl(context):
    context.driver.find_element(By.ID, 'close-button').click()
