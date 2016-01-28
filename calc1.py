from selenium import webdriver
from selenium.webdriver.common.keys import Keys



browser = webdriver.Firefox()
browser.get('http://jeremydomasian.github.io/supercalc_v1-4/SuperCalc-v3.html')

#input email 
clearElem = browser.find_element_by_name('clear')
clearElem.click()

print "yay"
