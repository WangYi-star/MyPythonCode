# -*- encoding: utf-8 -*-
'''
@File : question2_file-read.py
@Time : 2020/03/20 10:36:59
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
写一个程序，从input.txt中读取之前输入的数据，
存入列表中，再加上行号打印显示；格式如下:
#第一行： xxxx
#第二行： xxxx
'''
list=[]
try:
    with open(r"notefile\input.txt",'r',encoding='utf-8') as f1:
        for line in f1.readlines():
            list.append(line.strip())
except FileNotFoundError as fnot:
    print(fnot)

for i,a in enumerate(list):
    print('第{}行：{}'.format(i+1,a))