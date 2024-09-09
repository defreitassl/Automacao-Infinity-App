import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = os.path.join(os.getcwd(), 'chromedriver-linux64', 'chromedriver')

service = Service(executable_path=driver_path)

driver = webdriver.Chrome(service=service)