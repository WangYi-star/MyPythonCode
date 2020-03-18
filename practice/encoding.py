# -*- encoding: utf-8 -*-
'''
@File : 1.17-prac3.py
@Time : 2020/03/18 10:04:54
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
import sys
print("文件系统编码格式：")
print(sys.getfilesystemencoding())

print("当前目录:")
cwd=os.getcwd()
print(cwd)
print(os.path.join(cwd,r"Pcode\hafka\ta.txt"))
print(os.path.abspath(os.path.join(cwd,r"Pcode\hafka\ta.txt")))
print("不设置编码格式:")
f1=open(r'E:\应用程序\Python\a-PythonProject\Pcode\hafka\ta.txt','r')
for line in f1.readlines():
    print(line.strip())
f1.close()
print("设置编码格式(gbk):")
f1=open(r'E:\应用程序\Python\a-PythonProject\Pcode\hafka\ta.txt','r',encoding='gbk')
for line in f1.readlines():
    print(line.strip())
f1.close()
print("设置编码格式(utf-8):")
f1=open(r'E:\应用程序\Python\a-PythonProject\Pcode\hafka\ta.txt','r',encoding='utf-8')
for line in f1.readlines():
    print(line.strip())
f1.close()
