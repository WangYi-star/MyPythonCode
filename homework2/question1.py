# -*- encoding: utf-8 -*-
'''
@File : question1.py
@Time : 2020/03/08 20:21:49
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。
'''
def instance(a):
    return len(a)
a=[1,2,3,4,5]
b=(1,2,3)
c="asdfewef"
print(instance(a))
print(instance(b))
print(instance(c))