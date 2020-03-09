# -*- encoding: utf-8 -*-
'''
@File : question4.py
@Time : 2020/03/08 20:53:51
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
'''
def statistic(str):
    a=0
    b=0
    c=0
    d=0
    for i in str:
        if i.isalpha():
            a+=1
        elif i.isdigit():
            b+=1
        elif i.isspace():
            c+=1
        else:
            d+=1
    print('字母有{}个'.format(a))
    print('数字有{}个'.format(b))
    print('空格有{}个'.format(c))
    print('其它字符有{}个'.format(d))

str='''fas wfwea 4654,af;asdf,?asdf.asdf5448as546sadfsf[,;as,adf,sd45'''
statistic(str)