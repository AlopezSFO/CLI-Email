from selenium import webdriver
from selenium.webdriver.common.keys import Keys


print('Lets go!')
userEmail = ('AngieAutoQA@yahoo.com')
userPassword = ('YUopty1!')


browser = webdriver.Firefox()
browser.get('https://login.yahoo.com/?.src=ym&.intl=us&.lang=en-US&.done=https%3a//mail.yahoo.com')

#input email 
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys(userEmail)

#input password
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys(userPassword)

signInElem = browser.find_element_by_id('login-signin')
signInElem.click()

print('Who do you want to email?')
userSend = raw_input()

print('What do you want your subject to be?')
userSubject = raw_input()
print('Type your message and hit Enter!')
userMessage = raw_input()

#click compose

composeElem = browser.find_element_by_id('Compose')
composeElem.click()

#click recipient and input
toElem = browser.find_element_by_id('to-field')
toElem.send_keys(userSend)
toElem.send_keys(Keys.ENTER);


subElem = browser.find_element_by_id('subject-field')
subElem.send_keys(userSubject)

#input string
messageElem = browser.find_element_by_id('rtetext')
messageElem.click()
messageElem.send_keys(userMessage)

#send!
sendElem = browser.find_element_by_class_name('default')
sendElem.click()