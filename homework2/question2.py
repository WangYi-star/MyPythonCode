# -*- encoding: utf-8 -*-
'''
@File : question2.py
@Time : 2020/03/08 20:25:58
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
编写一个函数,接收n个数字，求这些参数数字的和;
'''
def getsum():
    sum=0;
    n=int(input("请输入数字个数："))
    print("请输入数字：")
    for i in range(0,n):
        sum=sum+int(input())
    print("数字求和：")
    print(sum)
getsum()
