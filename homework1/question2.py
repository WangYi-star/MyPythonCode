# -*- encoding: utf-8 -*-
'''
@File : question2.py
@Time : 2020/03/05 13:28:36
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
dict={"key":("1101","1102","1103","1104","1105","1106","1107","1108","1109","1110"),\
    "value":(54,65,84,75,99,42,58,88,92,96)}
print("分数大于80的同学如下：")
for a in range(0,10):
    if(dict["value"][a]>80):
        print(dict["key"][a],dict["value"][a])