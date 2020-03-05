# -*- encoding: utf-8 -*-
'''
@File : question3.py
@Time : 2020/03/05 13:40:15
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
list1=[12,42,1,84,52,45,62,75,23,78]
list2=[44,42,12,55,94,86,75,33,52,9]
list3=[a for a in list1 if a in list2]
print("list1、list2相同的元素如下：")
print(list3)