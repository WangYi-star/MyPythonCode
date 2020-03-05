# -*- encoding: utf-8 -*-
'''
@File : question10.py
@Time : 2020/03/05 19:40:54
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
str='''If you have been asking yourself what the best solution for gaming was,anormal in desk or a standing one,the right answer\
 is neither.In fact,after feasting your eyes on gaming bed.'''
print("\n英文文本：")
print(str)
str1=str.replace(","," ")
str2=str1.replace("."," ")
str3=str2.lower()
str4=str3.rstrip()
list1=str4.split(" ")
dict={}
for a in list1:
    if a in dict.keys():
        dict[a]=dict[a]+1
    else:
        dict[a]=1
list2=list(dict.items())
size = lambda  pl: pl[1]
list2.sort(key=size,reverse=True)
print("\n单词统计:")
for a in list2:
    print('{} : {}'.format(a[0],a[1]))
