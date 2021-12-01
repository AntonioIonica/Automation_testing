from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('C:/Users/anton/PycharmProjects/Automation_testing/src/Formy/chromedriver.exe')


@given(u'I open the website')
def websiteOpen(context):
    context.driver = webdriver.Chrome(service=service)
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
    context.driver.close()
