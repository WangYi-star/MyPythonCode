# -*- encoding: utf-8 -*-
'''
@File : question6.py
@Time : 2020/03/08 21:28:10
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
定义一个函数, 打印输出n以内的斐波那契数列;
'''
def solve(n):
    a=[1,1]
    while 1:
        if a[len(a)-2]+a[len(a)-1]<=n:
            a.append(a[len(a)-2]+a[len(a)-1])
        else:
            break
    for i in a:
        print(i,end=" ")

print("打印n以内的斐波那契数列")
n=int(input("请输入数字n："))
solve(n)