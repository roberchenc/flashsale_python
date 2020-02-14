# -*- coding: utf-8 -*-
# author : ccl
# 小米有品抢购

from selenium import webdriver
import datetime
import time

#创建浏览器对象
driver = webdriver.Chrome()
#窗口最大化显示
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(2)

driver.get("https://www.xiaomiyoupin.com/detail?gid=118416&spmref=YouPinPC.$SearchFilter$1.search_list.2.25436327")

time.sleep(30)
while True:
    try:
        # 找到“立即购买”，点击
        if driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[1]/div[1]/div[2]/div[7]/div[1]/a[2]'):
            driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[1]/div[1]/div[2]/div[7]/div[1]/a[2]').click()
            break
        time.sleep(0.1)
    except:
        time.sleep(0.3)

driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div[2]/div[6]/a').click()
