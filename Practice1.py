from selenium import webdriver


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

#click sign in button
signInElem = browser.find_element_by_id('login-signin')
signInElem.click()

#click compose
buttonElem = browser.find_element_by_id('yui_3_16_0_1_1453316166049_1561')
buttonElem.click()

#click in text box

#print string

#input string