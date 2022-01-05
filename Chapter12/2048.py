from selenium import webdriver
import sys,time
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://play2048.co/')
start=browser.find_element_by_class_name('feedback-button')
while True:
    start.send_keys(Keys.UP)
    start.send_keys(Keys.RIGHT)
    start.send_keys(Keys.DOWN)
    start.send_keys(Keys.LEFT)

        
