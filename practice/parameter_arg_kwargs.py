# -*- encoding: utf-8 -*-
'''
@File : prac4.py
@Time : 2020/03/06 09:42:07
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def pack1(*a):
    print(list(a))

def pack2(**a):
    print(a)

pack1(1,2,5,4,8,6,5)
pack1(*(1,2,5,4,8,6,5))#传元组
pack2(a=1,b=2,c=3)
pack2(**{"a":1,"b":2,"c":3})#传字典