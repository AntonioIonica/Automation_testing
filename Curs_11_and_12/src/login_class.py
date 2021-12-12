"""
Login test case
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service = Service('//chromedriver.exe')

navi = (By.CSS_SELECTOR, '#content > ul > li:nth-child(21) > a')
usr = (By.ID, 'username')
pwd = (By.ID, 'password')
login_btn = (By.CSS_SELECTOR, '#login > button')
logout_btn = (By.CSS_SELECTOR,'#content > div > a')
error_login = (By.ID, 'flash-messages')

driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/')
time.sleep(2)
driver.find_element(*navi).click()

# invalid login

driver.find_element(*usr).send_keys('orice')
time.sleep(2)
driver.find_element(*pwd).send_keys('ptest')
time.sleep(2)
driver.find_element(*login_btn).click()

alerta = driver.find_element(*error_login).text
if 'Your username is invalid' in alerta:
    print('Test invalid login passed')
time.sleep(2)

# valid login

driver.find_element(*usr).send_keys('tomsmith')
time.sleep(2)
driver.find_element(*pwd).send_keys('SuperSecretPassword!')
time.sleep(2)
driver.find_element(*login_btn).click()
time.sleep(2)
driver.find_element(*logout_btn).click()

time.sleep(2)
driver.quit()