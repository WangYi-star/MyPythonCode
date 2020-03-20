# -*- encoding: utf-8 -*-
'''
@File : q6.py
@Time : 2020/03/20 17:30:28
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
在2个文件中存放了英文计算机技术文章
(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章),
请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
比较这2篇文章的相似度
(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);
'''


str1=""
str2=""
try:
    with open(r"notefile\text1.txt",'r',encoding='utf-8') as f1:
        for line in f1.readlines():
            str1=str1+line.strip()
except FileNotFoundError as fnot:
    print(fnot)

try:
    with open(r"notefile\text2.txt",'r',encoding='utf-8') as f2:
        for line in f2.readlines():
            str2=str2+line.strip()
except FileNotFoundError as fnot:
    print(fnot)

str1=str1.lower()
str2=str2.lower()
zf=",.?()[]"
for a in str1:
    if a in zf:
        str1=str1.replace(a," ")
for a in str2:
    if a in zf:
        str2=str2.replace(a," ")
list1=str1.split(" ")   
while 1:
    if '' in list1:
        list1.remove('')
    else:
        break

list2=str2.split(" ")
while 1:
    if '' in list2:
        list2.remove('')
    else:
        break

dict1={}
dict2={}
for a in list1:
    if a not in dict1:
        dict1[a]=1
    else:
        dict1[a]+=1

for a in list2:
    if a not in dict2:
        dict2[a]=1
    else:
        dict2[a]+=1
list1=list(dict1.items())
list2=list(dict2.items())
list1.sort(key=lambda p:p[1],reverse=True)
list2.sort(key=lambda p:p[1],reverse=True)
try:
    with open(r"notefile\data1.txt",'w',encoding='utf-8') as f3:
        for a in list1:
            str1=a[0]+"  "+str(a[1])+"\n"
            f3.write(str1)
except FileNotFoundError as fnot:
    print(fnot)

try:
    with open(r"notefile\data2.txt",'w',encoding='utf-8') as f4:
        for a in list2:
            str1=a[0]+"  "+str(a[1])+"\n"
            f4.write(str1)
except FileNotFoundError as fnot:
    print(fnot)
list3=list1[0:10]
list4=list2[0:10]
print("词频最高的前10个词：")
for a in range(10):
    print('{:>7} : {:<2}             {:>7} : {:<2}'.format(list1[a][0],list1[a][1],list2[a][0],list2[a][1]))
list5=[]
for a in list3:
    for b in list4:
        if a[0]==b[0]:
            list5.append(a)
print("\n相似度高的单词：")
for a in list5:
    print(a[0])
print('\n两篇文章的相似度为{}%'.format(len(list5)*10))

