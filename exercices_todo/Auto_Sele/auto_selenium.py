"""
Just a test to see the methods
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('/chromedriver.exe')
chrome_browser = webdriver.Chrome(service=service)

chrome_browser.maximize_window()
chrome_browser.get('https://formy-project.herokuapp.com/form')

time.sleep(2)

element = chrome_browser.find_element(By.ID, 'first-name')
element.clear()
element.send_keys('Andrei')
chrome_browser.find_element(By.XPATH, '/html/body/div/form/div/div[8]/a').click()

chrome_browser.close()

