# -*- encoding: utf-8 -*-
'''
@File : q5.py
@Time : 2020/03/20 17:04:26
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
list1=[]
try:
    with open(r"notefile\Blow in the wind.txt",'r',encoding='utf-8') as f1:
        for line in f1.readlines():
            list1.append(line.strip())
except FileNotFoundError as fnot:
    print(fnot)

try:
    with open(r"notefile\Blow in the wind.txt",'w',encoding='utf-8') as f2:
        list1.insert(0,"Blow in the wind")
        list1.insert(1,"Bob Dylan")
        list1.append("1962 by Warner Bros.Inc")
        for a in list1:
            f2.write(a)
            f2.write("\n")
except FileNotFoundError as fnot:
    print(fnot)

try:
    with open(r"notefile\Blow in the wind.txt",'r',encoding='utf-8') as f3:
        for line in f3.readlines():
            print(line.strip())
except FileNotFoundError as fnot:
    print(fnot)


    