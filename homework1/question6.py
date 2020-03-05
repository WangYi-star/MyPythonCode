# -*- encoding: utf-8 -*-
'''
@File : question6.py
@Time : 2020/03/05 17:20:15
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
list=[0,2]
for a in range(2,100):
    b=list[a-1]+list[a-2]
    if b<=100:
        list.append(b)
    else:
        break
print("斐波那契数列如下：")
print(list)