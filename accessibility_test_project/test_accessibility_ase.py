"""
Accessibility testing using Axe selenium python tool on
https://www.ase.ro/ webpage
"""

from selenium import webdriver
from axe_selenium_python import Axe


url = 'https://www.ase.ro/'
driver = webdriver.Chrome()

driver.get(url)
axe = Axe(driver)
# Inject axe in the the webpage
axe.inject()
# Running axe script
results = axe.run()
# writing json file for results
axe.write_results(results, 'ase_access.json')

driver.close()
assert len(results["violations"]) == 0, axe.report(results["violations"])

driver.quit()
