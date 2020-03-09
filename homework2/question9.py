# -*- encoding: utf-8 -*-
'''
@File : question9.py
@Time : 2020/03/09 17:19:57
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);
'''
def list_sort1(a):        
    a.sort(key=lambda p:p)
    print(a)

def list_sort2(a):         #冒泡排序
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
    print(a)

list=[2,4,5,1,8,75,12,41,25,65]
list_sort1(list)
list_sort2(list)