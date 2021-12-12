import time

from behave import *
from selenium.webdriver.common.by import By


@given('I open Google maps website')
def openWebsite(context):
    context.driver.get('https://www.google.com/')
    context.driver.maximize_window()
    context.driver.find_element(By.ID, 'L2AGLb').click()
    time.sleep(3)
    google_maps = context.driver.find_element(By.XPATH,
                                              '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    google_maps.send_keys('Google maps')
    google_maps.submit()
    context.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/h3').click()


@when('I click on Search bar')
def clickSearchBar(context):
    print('test')
    context.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]').click()


@when('I enter the input "{cities}"')
def enterInput(context, cities):
    context.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys(cities)
    time.sleep(5)


@then('First suggestion should be "{suggestions}"')
def suggestionPop(context, suggestions):
    cities_suggestion = context.driver.find_element(By.ID, 'sbsg50').text
    if suggestions in cities_suggestion:
        assert True, 'Test Passed!'
    else:
        assert False, 'Test Failed!'
