# -*- encoding: utf-8 -*-
'''
@File : q1_run-time.py
@Time : 2020/04/06 17:34:48
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
编写一个装饰器，能计算其他函数的运行时间；
'''
import time
from collections import deque

def runtime(func):
    def mainfunc(*arg,**kw):
        start_time=time.time()
        print('start time:',start_time)
        func(*arg,**kw)
        end_time=time.time()
        print('end time',end_time)
        print('run time：{}s'.format(end_time-start_time))
    return mainfunc

@runtime
def function1():
    deque_list=deque(list(range(50)))
    deque_list.popleft()
    deque_list.appendleft('deque')
    print(deque_list)

function1()    
