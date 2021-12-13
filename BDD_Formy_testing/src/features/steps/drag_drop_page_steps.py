import time
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@when(u'I navigate to drag and drop')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/li[5]/a').click()
    time.sleep(2)


@when(u'I drag and drop it on the box area')
def step_impl(context):
    source1 = context.driver.find_element(By.XPATH, '//*[@id="image"]/img')
    source2 = context.driver.find_element(By.ID, 'box')
    try:
        ActionChains(context.driver).drag_and_drop(source1, source2).perform()
    except:
        print('Action not performed')
        assert False
    time.sleep(1)


@then(u'The image "Se" should be in the box')
def step_impl(context):
    check_drag = context.driver.find_element(By.XPATH, '//*[@id="box"]/p').text
    if check_drag == 'Drop here':
        assert False
