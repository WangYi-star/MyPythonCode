# -*- encoding: utf-8 -*-
'''
@File : question1.py
@Time : 2020/03/05 13:01:30
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
list1=[a for a in range(0,51) if a%2==1]
print("0-50之间的奇数如下：")
print(list1)
list2=[a for a in range(0,51) if a%2==0]
print("0-50之间的偶数如下：")
print(list2)
list3=[2]
for a in range(3,51):
    flag=1
    for b in range(2,a):
        if(a%b==0):
            flag=0;
            break;
    if flag==1:
        list3.append(a)
print("0-50之间的质数如下：")
print(list3)
list4=[a for a in range(0,51) if a%2==0 and a%3==0]
print("0-50之间能同时被2和3整除的数如下：")
print(list4)




