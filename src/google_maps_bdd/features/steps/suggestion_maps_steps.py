from behave import *
from selenium.webdriver.common.by import By


@given('I open Google maps website')
def openWebsite(context):
    context.driver.get('https://www.google.com/maps')
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div/div/button').click()


@when('I click on Search bar')
def clickSearchBar(context):
    context.driver.find_element(By.ID, 'searchboxinput').click()


@when('I enter the input "{cities}"')
def enterInput(context, cities):
    context.driver.find_element(By.ID, 'searchboxinput').send_keys(cities)


@then('First suggestion should be "{suggestions}"')
def suggestionPop(context, suggestions):
    cities_suggestion = context.driver.find_element(By.ID, 'sbsg50').text
    if suggestions in cities_suggestion:
        assert True, 'Test Passed!'
    else:
        assert False, 'Test Failed!'
