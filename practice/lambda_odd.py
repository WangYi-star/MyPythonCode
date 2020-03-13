# -*- encoding: utf-8 -*-
'''
@File : prac3.py
@Time : 2020/03/06 08:43:09
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
list1=list(range(1,21))
print("原列表：")
print(list1)
res=filter(lambda a:a%2==1,list1)
print(type(res))
print("匿名函数求奇数：")
print(list(res))
list2=[a for a in list1 if a%2==1]
print("列表解析式求奇数：")
print(list2)
#res2=map(lambda a:a%2==1,list1)
#print(list(res2))
