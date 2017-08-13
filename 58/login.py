# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 00:19:57 2017

@author: wahlmzr
"""


from selenium import webdriver
driver = webdriver.Firefox()
url = 'https://passport.58.com/login/?path=http%3A//sh.58.com/%3Fpts%3D1490199757937&PGTID=0d100000-0000-2929-1860-57f22b65f83d&ClickID=1'
driver.get(url)

ele = driver.find_element_by_id('pwdLogin')
ele.click()

ele = driver.find_element_by_id('usernameUser')

ele.clear()
ele.send_keys('18917595376')



ele = driver.find_element_by_xpath('//*[@id="passwordUser"]')
ele.click()
ele.clear()
ele.send_keys('1987425')

ele = driver.find_element_by_id('btnSubmitUser')
ele.click()


