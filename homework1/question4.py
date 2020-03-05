# -*- encoding: utf-8 -*-
'''
@File : question4.py
@Time : 2020/03/05 13:59:05
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
a=int(input("请输入一个年份："))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("%d是闰年" % a)
        else:
            print("%d不是闰年" % a)
    else:
        print("%d是闰年" % a)
else:
    print("%d不是闰年" % a)