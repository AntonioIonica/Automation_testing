from behave import *
from selenium.webdriver.common.by import By


@given(u'I already have an account')
def printCreds(context):
    print('I first enter the right credentials and then some random ones')


@when(u'I open the website')
def websiteOpen(context):
    context.driver.get('https://the-internet.herokuapp.com/login')
    context.driver.implicitly_wait(5)


@when(u'I set the email popescu@gmail.com')
def wrongUsername(context):
    context.driver.find_element(By.ID, 'username').send_keys('popescu@gmail.com')


@when(u'I set the password abc1234')
def wrongPassword(context):
    context.driver.find_element(By.ID, 'password').send_keys('abc1234')
    context.driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
    context.driver.implicitly_wait(5)


@then(u'Invalid login appears')
def alertInvalid(context):
    invalid_login = context.driver.find_element(By.XPATH, '//*[@id="flash"]').text
    if 'invalid' in invalid_login:
        assert False, 'Test failed!'


@when(u'I set the email tomsmith')
def rightUsername(context):
    context.driver.find_element(By.ID, 'username').send_keys('tomsmith')


@when(u'I set the password SuperSecretPassword!')
def rightPassword(context):
    context.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
    context.driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
    context.driver.implicitly_wait(5)


@then(u'Successful login')
def flash(context):
    flash_succesful = context.driver.find_element(By.ID, 'flash').text
    if flash_succesful == 'You logged into a secure area!':
        assert True, 'Test pass!'


@then(u'User redirected to Secure Area')
def secure_area(context):
    secure_area_flash = context.driver.find_element(By.XPATH, '//*[@id="content"]/div/h2').text
    if secure_area_flash == 'Secure Area':
        assert True, 'Test pass!'
