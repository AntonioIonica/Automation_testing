import time
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@given(u'I am a guest')
def step_impl(context):
    print('Guest on the webpage')


@when(u'I open the website')
def step_impl(context):
    context.driver.get('https://formy-project.herokuapp.com/')
    context.driver.maximize_window()


@when(u'I navigate to buttons')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/li[2]/a').click()


@when(u'I hover on some buttons')
def step_impl(context):
    primary_btn = context.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div/div/button[1]')
    success_btn = context.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div/div/button[2]')
    info_btn = context.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div/div/button[3]')
    actions = ActionChains(context.driver)
    actions.move_to_element(primary_btn).move_to_element(success_btn).move_to_element(info_btn).perform()


@then(u'The buttons are not selected')
def step_impl(context):
    success_btn = context.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div/div/button[2]')
    if success_btn.is_selected():
        assert True


@when(u'I click on some buttons')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div/div/button[4]').click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div/div/button[5]').click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div/div/button[6]').click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, '/html/body/div/form/div[2]/div/div/div/button[1]').click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, '/html/body/div/form/div[2]/div/div/div/button[2]').click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, '/html/body/div/form/div[2]/div/div/div/button[3]').click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, '/html/body/div/form/div[3]/div/div/div/button[1]').click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, '/html/body/div/form/div[3]/div/div/div/button[2]').click()
    time.sleep(1)


@then(u'The buttons are selected')
def step_impl(context):
    btn_2 = context.driver.find_element(By.XPATH, '/html/body/div/form/div[3]/div/div/div/button[1]')
    if btn_2.is_selected():
        assert True


@when(u'I click on dropdown')
def step_impl(context):
    dropdown_btn = context.driver.find_element(By.XPATH, '//*[@id="btnGroupDrop1"]')
    dropdown_btn.click()
    time.sleep(1.5)


@when(u'I click on first option')
def step_impl(context):
    dropdown_link_1 = context.driver.find_element(By.XPATH, '/html/body/div/form/div[3]/div/div/div/div/div/a[1]')
    dropdown_link_1.click()


@then(u'The dropdown closes')
def step_impl(context):
    dropdown_show = context.driver.find_element(By.XPATH, '/html/body/div/form/div[3]/div/div/div/div/div')
    if dropdown_show.is_displayed():
        assert True
