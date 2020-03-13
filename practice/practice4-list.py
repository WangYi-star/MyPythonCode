# -*- encoding: utf-8 -*-
'''
@File : practice4-list.py
@Time : 2020/02/28 19:50:04
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
list=[56.23,54.2,89,97,65,85,75.46]
print("max=",end="")
print(max(list))
print("min=",end="")
print(min(list))
print("sum=",end="")
print(sum(list))
print("ave=",end="")
print(sum(list)/len(list))
list.sort()
print(list)
