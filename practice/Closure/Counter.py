# -*- encoding: utf-8 -*-
'''
@File : Counter.py
@Time : 2020/04/04 10:44:50
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
利用闭包返回一个计数器函数，每次调用它返回递增整数
'''
s=0
def log():
    global s
    s=0
    def countnum():
        global s
        s=s+1
        return s
    return countnum

countA=log()
print(countA(),countA(),countA(),countA(),countA())
countB=log()
print(countB(),countB(),countB(),countB(),countB())
        