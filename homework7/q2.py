# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2020/4/18 20:09
# Tool ：PyCharm
import os
import requests
from bs4 import BeautifulSoup
import re

path=r'E:\应用程序\Python\b-Python Crawler\crawler-data\url_tar.txt'
url_list=[]
with open(path,'r',encoding='utf-8')as f1:
    while 1:
        text=f1.readline().strip().strip()
        if not text:
            break
        url_list.append(text)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
a_list = []
for url in url_list:
    try:
        text=requests.get(url,headers=headers).content.decode('utf-8')
    except Exception as e1:
        print(e1)
    else:
        soup=BeautifulSoup(text,'html.parser')
        target=soup.find_all('a',text=re.compile(r'关于我们|企业介绍|企业发展|历史|概况'))
        for a in target:
            try:
                u=a.attrs['href']
            except:
                pass
            else:
                a_list.append(u)

for a in a_list:
    print(a)

