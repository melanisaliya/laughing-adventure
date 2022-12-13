from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

driver.get('https://185.215.180.7/mine?wallet=00CE531A7446ED8B039ADBF28EC66CA65C4770959A8E2E078A')
sleep(86400)
