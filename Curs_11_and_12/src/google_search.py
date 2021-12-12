"""
Google search script
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('//chromedriver.exe')

chrome_driver = webdriver.Chrome(service=service)
chrome_driver.maximize_window()
chrome_driver.get('https://www.google.com/')

time.sleep(2)

chrome_driver.find_element(By.ID, 'L2AGLb').click()

search_form = chrome_driver.find_element(By.NAME, 'q')
search_form.send_keys('Cheese')
time.sleep(1.5)
search_form.submit()
time.sleep(1.5)
chrome_driver.refresh()
time.sleep(1.5)
chrome_driver.quit()
