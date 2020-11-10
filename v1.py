from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains  import ActionChains
from selenium.common.exceptions import NoSuchElementException


import time
nameList = []

driver = webdriver.Chrome()

driver.get("http://gs.amac.org.cn/amac-infodisc/res/pof/member/index.html")
time.sleep(6)
driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()

select = driver.find_element_by_name('managerList_length')
select.find_element_by_xpath('//*[@id="managerList_length"]/label/select/option[4]').click()
##time.sleep(4)
window_before = driver.window_handles[0]
for y in range(1,42):

    for x in range(1,101):   
        
        
        
        try:
            dsa = "//*[@id='managerList']/tbody/tr["+str(x)+"]/td[2]/a"
            driver.find_element_by_xpath(dsa).click()
            window_after = driver.window_handles[1] 
            driver.switch_to.window(window_after)
            ##b=driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[1]/div[2]/table/tbody/tr[4]/td[2]')
            for i in range(1,8):
                try:
                    qwe = "/html/body/div[3]/div/div[4]/div/div[2]/table/tbody/tr["+str(i)+"]/td[1]"
                    ewq = "/html/body/div[3]/div/div[4]/div/div[2]/table/tbody/tr["+str(i)+"]/td[2]"
                    dd=driver.find_element_by_xpath(qwe)
                    ddd = dd.text
                    if ddd =="成立时间":
                        i = 8
                        b = driver.find_element_by_xpath(ewq)
                        
                
                        c=(b.text)
                        d=int(c[0:4])

                    
                        if d>=2019:
                            ele = driver.find_element_by_xpath('//*[@id="complaint2"]')
                            nameList.append(ele.text)

                            driver.close()
                            driver.switch_to.window(window_before)
                        else:
                            driver.close()
                            driver.switch_to.window(window_before)
                except NoSuchElementException:
                   pass
            
        except NoSuchElementException:
            pass
            

        

 
    driver.find_element_by_xpath('//*[@id="managerList_paginate"]/a[3]').click()
    time.sleep(2)

with open('asdnew.txt', 'w',encoding="utf-8") as f:
    for item in nameList:
        f.write("%s\n" % item)

