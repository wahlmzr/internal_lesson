# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:10:57 2017

@author: wahlmzr
"""

import numpy as np 
from selenium import webdriver
driver = webdriver.Firefox()
#driver.get('http://sh.58.com/job/pn2/')
#
#
#driver.find_element_by_xpath('//*[@id="jingzhun"]/dt/a').click()
#
#driver.switch_to_window(driver.window_handles[1])
#
#driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[6]/span/a[1]').click()
#
#
#cookie= driver.get_cookies()#获取登录成功后浏览器cookies

driver.delete_all_cookies()#删除所有的cookies
cookie = dict(np.load('cookie.npy'))
driver.add_cookie(cookie)#增加cookies

#cookie2=driver.get_cookies()#在查浏览器cookies，发现cookies值已经修改
url = 'http://sh.58.com/job/pn2/'
driver.get(url)#打开url，实现免登陆

driver.quit()