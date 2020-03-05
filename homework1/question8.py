# -*- encoding: utf-8 -*-
'''
@File : question8.py
@Time : 2020/03/05 17:50:22
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#工号，姓名，工龄，工资； 
#list1=list(dict.items())
list=[(2201," 李静如",2,2015),(2202," 王丽颖",3,5521),(2203,"张红涛",5,4521),(2204,"肖浩然",5,4444),(2205,"王林瑞",4,5626),\
    (2206,"朱介元",6,8452),(2207,"刘希平",4,3541),(2208," 李兰芳",5,10221),(2209,"张佳玉",2,8100),(2210,"程冠文",3,4456)]
size = lambda  pl: pl[3]
list.sort(key=size,reverse=True)
print(" 工号     姓名    工龄  工资")
for a in list:
    print('{:>5}  {:>6}  {:>2}  {:>6}'.format(a[0],a[1],a[2],a[3]))

