# -*- encoding: utf-8 -*-
'''
@File : calculate.py
@Time : 2020/04/04 16:03:23
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
定义一个高阶函数, 实现加,减,乘,除计算器功能;
'''
def jiafa(x,y):
    return x+y

def chengfa(x,y):
    return x*y

def jianfa(x,y):
    return x-y

def chufa(x,y):
    if(y==0):
        print('除数不能为零！')
        return
    else:
        return x/y
    
def solve(x,y,func):
    return func(x,y)

a=int(input('请输入一个数字：'))
b=input('请选择一个操作（+,-,*,/）:')
c=int(input('请输入另一个数字：'))
if b=='+':
    print(solve(a,c,jiafa))
elif b=='-':
    print(solve(a,c,jianfa))
elif b=='*':
    print(solve(a,c,chengfa))
elif b=='/':
    print(solve(a,c,chufa))
