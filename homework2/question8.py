# -*- encoding: utf-8 -*-
'''
@File : question8.py
@Time : 2020/03/09 17:05:45
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
请用Python定义一个函数，给定一个字符串，
找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
'''
def solve_max(str):
    a={}
    for i in str:
        if i in a.keys():
            a[i]+=1
        else:
            a[i]=1
    list1=list(a.items())
    list1.sort(key=lambda p:p[1],reverse=True)
    print('字符串中出现次数最多的字符为{}'.format(list1[0][0]))
    print('次数最多为{}次'.format(list1[0][1]))     

str="asdfwasasdfawasdfaswasfsad"
solve_max(str)       