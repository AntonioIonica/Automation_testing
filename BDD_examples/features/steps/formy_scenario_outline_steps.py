from behave import *
from selenium.webdriver.common.by import By


@given(u'I open the website')
def websiteOpen(context):
    context.driver.get('https://the-internet.herokuapp.com/login')
    context.driver.implicitly_wait(5)


@when(u'I enter the input "{user}" and "{password}"')
def usrInput(context, user, password):
    context.driver.find_element(By.ID, 'username').send_keys(user)
    context.driver.find_element(By.ID, 'password').send_keys(password)


@when(u'I click on login')
def clickLogin(context):
    context.driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
    context.driver.implicitly_wait(5)


@then(u'Display "{login_status}"')
def displayStatus(context, login_status):
    print(f'Yours credentials were {login_status}')

# TODO Allure reports
