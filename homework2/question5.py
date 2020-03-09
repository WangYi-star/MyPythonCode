# -*- encoding: utf-8 -*-
'''
@File : question5.py
@Time : 2020/03/08 21:16:25
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
'''

def solvedict(dict):
    for k,v in dict.items():
        if(len(v)>2):
            i=v[0:2]
            dict[k]=i
dict={"A":"asdf","B":["a","d","d"],"C":"as"}
print("修改前字典如下：")
print(dict)
solvedict(dict)
print("修改后字典如下：")
print(dict)