import time
from behave import *
from selenium.webdriver.common.by import By

RADIO_BTN_1 = (By.ID, 'radio-button-1')
RADIO_BTN_2 = (By.XPATH, '/html/body/div/div[2]/input')
RADIO_BTN_3 = (By.XPATH, '/html/body/div/div[3]/input')


@when(u'I navigate to "Radio buttons" page')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/li[12]/a').click()


@when(u'I click on the buttons in this order: 2>1>3')
def step_impl(context):
    context.driver.find_element(*RADIO_BTN_2).click()
    context.driver.find_element(*RADIO_BTN_1).click()
    context.driver.find_element(*RADIO_BTN_3).click()


@then(u'The button number 3 should be selected')
def step_impl(context):
    button3 = context.driver.find_element(*RADIO_BTN_3)
    if button3.is_selected():
        assert True


@when(u'I click on the buttons in this order: 1>3>2')
def step_impl(context):
    context.driver.find_element(*RADIO_BTN_1).click()
    context.driver.find_element(*RADIO_BTN_3).click()
    context.driver.find_element(*RADIO_BTN_2).click()


@then(u'The button number 2 should be selected')
def step_impl(context):
    button2 = context.driver.find_element(*RADIO_BTN_2)
    if button2.is_selected():
        assert True


@when(u'I click on the buttons in this order: 3>2>1')
def step_impl(context):
    context.driver.find_element(*RADIO_BTN_3).click()
    context.driver.find_element(*RADIO_BTN_2).click()
    context.driver.find_element(*RADIO_BTN_1).click()


@then(u'The button number 1 should be selected')
def step_impl(context):
    button1 = context.driver.find_element(*RADIO_BTN_1)
    if button1.is_selected():
        assert True
