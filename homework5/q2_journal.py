# -*- encoding: utf-8 -*-
'''
@File : q2_journal.py
@Time : 2020/04/06 17:56:47
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；
'''

def log(func):
    def mainfunc(*arg,**kw):
        func_call='call '+func.__name__+'()'
        print(func_call)
        with open(r'notefile/data1.txt','w',encoding='utf-8') as f1:
            f1.write(func_call)
            f1.write('\n')
        return func(*arg,**kw)
    return mainfunc

@log
def function1(x,y):
    return x+y

function1(12,15)
