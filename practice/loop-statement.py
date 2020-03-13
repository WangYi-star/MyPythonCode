# -*- encoding: utf-8 -*-
'''
@File : loop-statement.py
@Time : 2020/03/13 17:03:01
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
list1=list(range(10))
print("原列表：")
print(list1)
print("偶数元素：")
for a in list1:
    if(a%2==0):
        print(a)
