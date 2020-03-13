# -*- encoding: utf-8 -*-
'''
@File : prac2.py
@Time : 2020/03/06 08:37:18
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def printlist(list):
    print("修改前list：")
    print(list)
    list.append([1,2,3])
    print("传参后list的id：")
    print(id(list))
    print("修改后list：")
    print(list)

list=[12,45,78]
print("传参前list的id：")
print(id(list))
printlist(list)