from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver
from selenium.webdriver.firefox import options

service = Service(executable_path=GeckoDriverManager().install())

options = 
driver = webdriver.Firefox(options=options)

driver.quit()


