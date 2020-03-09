# -*- encoding: utf-8 -*-
'''
@File : question3.py
@Time : 2020/03/08 20:41:27
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
编写一个函数, 传入一个数字列表, 输出列表中的奇数;
数字列表请用随机数函数生成;
'''
def solve(a):
    print("列表中奇数如下：")
    list=[b for b in a if b%2==1]
    print(list)
    for i in range(len(a)):
        if(a[i]%2==1):
            print(a[i],end=" ")
    

import random
list1=[random.randint(1,100) for i in range(30)]
print("列表如下：")
print(list1)
solve(list1)