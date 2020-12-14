# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 09:23:24 2020

@author: cis-user
"""

from selenium import webdriver
import csv
import requests
from bs4 import BeautifulSoup
import time,datetime
import sys
from selenium.webdriver.support.ui import Select

url="https://www.ettoday.net/news/news-list.htm"

options=webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_options=options)
driver.get(url)

now = datetime.datetime.now() #now=現在的時間
oneday = datetime.timedelta(days=5)#設定為5天

# now= now-oneday #今天之前的5天

page=0
with open('抓五天新聞.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('日期','分類','連結'))
    writer.writerow(['標題'])
    
    for i in range(5):
        page+=1
        html = driver.page_source
        sp=BeautifulSoup(html,"html.parser")
        search_h3=sp.select("div.part_list_2 > h3 > a")#標題跟網址用
        search_a=sp.select("div.part_list_2 > h3 > span")#時間
        search_b=sp.select("div.part_list_2 > h3 > em")#分類
        
        for i in range(5):  #怕跑太久，每天先抓五個新聞
            print(page)
            print(search_a[i].text,end=' ')
            print(search_b[i].text,end=' ')
            print(search_h3[i].text,end=' ')
            print(search_h3[i].get('href'))#抓網址
            
            writer.writerow([search_a[i].text,search_b[i].text,search_h3[i].get('href')])
            writer.writerow([search_h3[i].text])
            
        one1= datetime.timedelta(days=1)
        now=now-one1
        ndate=now.strftime('%Y%m%d')#抓出now的年月日
        a=ndate[-2:]
        
        a=int(a)#避免7號變成07號
        a=str(a)
        
        b=ndate[-4:-2]
        
        b=int(b)#避免7月變成07月
        b=str(b)   
        
        driver.find_element_by_id("selM").click()
        Select(driver.find_element_by_id("selM")).select_by_visible_text(b)
        driver.find_element_by_id("selM").click()
        driver.find_element_by_id("selD").click()
        Select(driver.find_element_by_id("selD")).select_by_visible_text(a)
        driver.find_element_by_id("selD").click()
        driver.find_element_by_id("button").click()
        
        time.sleep(2)  #動作太快會出錯,所以要加入等待時間
    
driver.close()               #關閉瀏覽器


sys.exit    
