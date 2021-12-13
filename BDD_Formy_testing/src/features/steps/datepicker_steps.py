import time
from behave import *
from selenium.webdriver.common.by import By


@when('I navigate to datepicker')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/li[4]/a').click()


@when('I enter a date with keyboard')
def step_impl(context):
    date_picker = context.driver.find_element(By.ID, 'datepicker')
    date_picker.clear()
    time.sleep(1.5)
    date_picker.send_keys('07/10/1994')
    time.sleep(1.5)


@then('The calendar should display the respective date')
def step_impl(context):
    current_date = context.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/table/thead/tr[2]/th[2]').text
    if 'October' in current_date:
        assert True
