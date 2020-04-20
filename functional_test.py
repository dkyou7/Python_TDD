from selenium import webdriver

driver = webdriver.Chrome('/Users/dkyou7/Desktop/dev/chromedriver')
driver.get('http://localhost:8000')

assert 'Django' in driver.title