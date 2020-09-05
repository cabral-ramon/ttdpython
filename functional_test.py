import os
from selenium import webdriver

gecko_driver_path = os.path.join(os.getcwd(), 'geckodriver.exe')
browser = webdriver.Firefox(executable_path=gecko_driver_path)
browser.get('http://localhost:8000')

assert 'Django' in browser.title

