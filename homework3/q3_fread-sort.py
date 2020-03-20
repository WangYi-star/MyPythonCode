# -*- encoding: utf-8 -*-
'''
@File : question3.py
@Time : 2020/03/20 10:50:35
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
编写一个程序，读取文件中保存的10个学生成绩名单信息
(学号,姓名, Python课程分数);
然后按照分数从高到低进行排序输出
'''
list=[]
try:
    with open(r"notefile\stu_score.txt",'r',encoding='utf-8') as f1:
        for line in f1.readlines():
            list1=line.strip().split(" ")
            list.append(list1)
except FileNotFoundError as fnot:
    print(fnot)
list.sort(key=lambda p:p[2],reverse=True)
print("学生成绩排序如下：")
for a in list:
    print('{}  {}  {}'.format(a[0],a[1],a[2]))
