# -*- encoding: utf-8 -*-
'''
@File : q2.py
@Time : 2020/04/27 21:57:30
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
   请查资料，Python的 requests库，如何判断一个网址可以访问；
提示 ：使用requests模块
   def getHtmlText(url):
    try:        # 网络连接有风险，异常处理很重要
        r = requests.get(url,timeout=30)    # 查一下这个方法的使用
        r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
         return "产生异常"
  数据文件（1000个网址）：
'''

from threading import Thread
from queue import Queue
import requests

def work(url_list):
    while not url_list.empty():
        url=url_list.get()
        try:
            respose=requests.get(url,timeout=10)
            respose.raise_for_status()
        except:
            print(url+'不能访问')


if __name__=='__main__':
    url_list=Queue()
    path=r'E:\应用程序\Python\b-Python Crawler\crawler-data\reurl.txt'
    with open(path,'r',encoding='utf-8')as f1:
        while True:
            text=f1.readline()
            if not text:
                break
            url_list.put(text.strip())
    for i in range(50):
        t=Thread(target=work,args=(url_list,))
        t.start()

