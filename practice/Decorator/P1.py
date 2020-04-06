# -*- encoding: utf-8 -*-
'''
@File : P1.py
@Time : 2020/04/04 10:12:39
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
定义一个函数, 做2个数的加法;  然后我们定义一个装饰器, 对原函数记录运行日志;
'''
def log(func):
    def wrapper(x,y):
        print('call %s()' % func.__name__)
        res=func(x,y)
        print('sum:%.2f' % res)
    return wrapper

@log
def sum(x,y):
    return x+y

sum(1,2)