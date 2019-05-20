# ! python3
# cle - sending emails with text provided by sys args


import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Getting Email adress and text message from CMD
email_adress = sys.argv[1]
email_text = ' '.join(sys.argv[2:])

browser = webdriver.Firefox()
browser.get('http://gmail.com')

# Fill my email adress
my_email = browser.find_element_by_class_name('whsOnd')
my_email.send_keys('bartosz.chojnacki4')
my_email.send_keys(Keys.ENTER)
time.sleep(5)

# Fill my password
my_pass = browser.find_element_by_name('password')
my_pass.send_keys('THU2tqQR%vUU:')
my_pass.send_keys(Keys.ENTER)
time.sleep(30)

# Click "Compose" Button
button = browser.find_element_by_xpath("//div[@gh='cm']")
button.click()
time.sleep(15)

# Fill field "To" with variable email_adress
fill = browser.find_element_by_name('to')
fill.send_keys(email_adress)
time.sleep(15)

content = browser.find_element_by_xpath('//div[@aria-label="Message Body"]')
content.click()
content.send_keys(email_text)
content.send_keys(Keys.LEFT_CONTROL+Keys.ENTER)
