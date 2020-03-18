# -*- encoding: utf-8 -*-
'''
@File : 1.17-prac2.py
@Time : 2020/03/18 09:06:53
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
print(os.getcwd())
print("绝对路径打开文件:")
f1=open(r'E:\应用程序\Python\a-PythonProject\Pcode\hafka\ta.txt','r',encoding='utf-8')
for line in f1.readlines():
    print(line.strip())
f1.close()
print("相对路径打开文件:")
print("(1):")
with open(r".\Pcode\hafka\ta.txt",'r',encoding='utf-8') as f2:
    for line in f2.readlines():
        print(line.strip())
print("(2):")
with open(r"Pypractice\wo.txt",'r',encoding='utf-8') as f3:
    for line in f3.readlines():
        print(line.strip())

