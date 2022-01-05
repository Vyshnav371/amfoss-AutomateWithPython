from selenium import webdriver
import sys,time
from selenium.webdriver.common.keys import Keys
#CLI
'''
receiver=sys.argv[1]
message=sys.argv[2]'''
#Manual
receiver='vyshnavunni371@gmail.com'
message='This is a Test'
browser = webdriver.Firefox()
email1='random0371@hotmail.com'
pass1='random371'
browser.get('https://outlook.live.com/owa/?nlp=1')
emailinput=browser.find_element_by_id('i0116')
emailinput.send_keys(email1)
emailinput.send_keys(Keys.ENTER)
time.sleep(1)
passinput=browser.find_element_by_id('i0118')
passinput.send_keys(pass1)
time.sleep(2)
passinput.send_keys(Keys.ENTER)
time.sleep(1)
signq=browser.find_element_by_id('idSIButton9')
time.sleep(2)
signq.click()
time.sleep(10)
newmsg = browser.find_element_by_id('id__6')
newmsg.click()
time.sleep(3)
to=browser.find_element_by_class_name('pickerInput_cc9894a7')
to.send_keys(receiver)
time.sleep(1)
subject=browser.find_element_by_id('TextField82')
subject.send_keys('Selenium message')
time.sleep(1)
content=browser.find_element_by_class_name('_3VQzn9yg47NIR2H1tIIeag')
content.send_keys(message)
time.sleep(2)
send = browser.find_element_by_id('id__87')
send.click()
