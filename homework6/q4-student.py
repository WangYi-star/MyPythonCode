# -*- encoding: utf-8 -*-
'''
@File : q4.py
@Time : 2020/04/10 00:20:16
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
封装方法，求单个学生的总分，平均分，以及打印学生的信息。
'''
class Student:
    def __init__(self,name,age,sex,score):
        self.__name=name
        self.__age=age
        self.__sex=sex
        self.__score=score

    def total_score(self):
        return sum(self.__score)

    def average_score(self):
        return sum(self.__score)/3

    def stu_message(self):
        print('学生信息：')
        print('姓名：',self.__name,'年龄：',self.__age,'性别：',self.__sex,\
        '分数：',self.__score[0],self.__score[1],self.__score[2])

stu1=Student('张三',20,'男',[86,74,56])
stu1.stu_message()
print('平均分：',stu1.average_score())
print('总分：',stu1.total_score())