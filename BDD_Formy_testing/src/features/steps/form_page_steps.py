import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@when('I click on Complete web form')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/li[14]/a').click()


@when('I type "{first_name}" as First name')
def step_impl(context, first_name):
    context.driver.find_element(By.ID, 'first-name').send_keys(first_name)


@when('I type "{last_name}" as Last name')
def step_impl(context, last_name):
    context.driver.find_element(By.ID, 'last-name').send_keys(last_name)


@when('I type "{job}" as Job title')
def step_impl(context, job):
    context.driver.find_element(By.ID, 'job-title').send_keys(job)


@when('I choose a form of education')
def step_impl(context):
    button1 = context.driver.find_element(By.ID, 'radio-button-1')
    button_state = button1.is_selected()
    print(f'HighSchool button state is {button_state}')
    if button_state:
        assert False
    button1.click()
    button_state = button1.is_selected()
    print(f'HighSchool button state is {button_state}')
    if button_state:
        assert True


@when('I choose a sex')
def step_impl(context):
    context.driver.find_element(By.ID, 'checkbox-1').click()


@when('I choose some years of experience')
def step_impl(context):
    element = context.driver.find_element(By.ID, 'select-menu')
    drp = Select(element)
    drp.select_by_index(1)


@when('I sent "{date}" as Date birth')
def step_impl(context, date):
    date_picker = context.driver.find_element(By.ID, 'datepicker')
    date_picker.clear()
    time.sleep(1.5)
    date_picker.send_keys(date)


@when('I click on submit')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'body > div > form > div > div:nth-child(15) > a').click()


@then('The form will be successfully submitted')
def step_impl(context):
    success = context.driver.find_element(By.XPATH, '/html/body/div/div').text
    if 'The form was successfully submitted!' in success:
        assert True, 'Test passed!'
    else:
        assert False, 'Test Failed'
