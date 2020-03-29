# -*- encoding: utf-8 -*-
'''
@File : q5.py
@Time : 2020/03/28 20:45:49
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
通过Python来模拟实现一个txt文件的拷贝过程;
'''
import os

def copy(path1,path2):
    str=""
    with open(path1,'r',encoding='utf-8') as f1:
        for line in f1.readlines():
            str=str+line
    with open(os.path.join(path2,os.path.basename(path1)),'w',encoding='utf-8') as f2:
            f2.write(str)
            
str1=input('请输入要拷贝文件的地址：')
str2=input('请输入要拷贝到的地址：')
copy(str1,str2)