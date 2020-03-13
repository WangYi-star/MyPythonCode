# -*- encoding: utf-8 -*-
'''
@File : practice8-input().py
@Time : 2020/03/04 08:22:34
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''
# here put the import lib

#将控制台输入的字符串,转换成元组, 并输出显示;

str=input("请输入字符串：")
list=str.split()
list1=[int(list[i]) for i in range(len(list))]
tup1=tuple(list1)
print(tup1)
