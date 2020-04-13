# -*- encoding: utf-8 -*-
'''
@File : q6.py
@Time : 2020/04/10 17:13:13
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
用面向对象,实现一个学生Python成绩管理系统;
学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
实现对学生信息及成绩的增,删,改,查方法;
'''

import os
import sys

class manage_student:
    def __init__(self):
        self.stu_list=[]
        with open(r'E:/应用程序/Python/a-PythonProject/notefile/python_score.txt','r',encoding='utf-8') as f1:
            while 1:
                text=f1.readline()
                if text:
                    self.stu_list.append(text.strip().split())
                else:
                    break

    def enter_message(self): # 添加
        message=input('请输入需要添加的学生信息（班级 学号 姓名 分数）：').split()
        self.stu_list.append(message)
        self.stu_list.sort(key=lambda p:p[1])
        with open(r'E:/应用程序/Python/a-PythonProject/notefile/python_score.txt','w',encoding='utf-8') as f2:
            for a in self.stu_list:
                f2.write(a[0]+' '+a[1]+' '+a[2]+' '+a[3])
                f2.write('\n')
        print('添加信息成功！')

    def delete_message(self): # 删除
        id=input('请输入要删除的学生的学号：')
        for i,a in enumerate(self.stu_list):
            if id==a[1]:
                self.stu_list.pop(i)
                with open(r'E:/应用程序/Python/a-PythonProject/notefile/python_score.txt','w',encoding='utf-8') as f2:
                    for a in self.stu_list:
                        f2.write(a[0]+' '+a[1]+' '+a[2]+' '+a[3])
                        f2.write('\n')
                print('删除信息成功！')
                return 
        print('不存在此学号！')
    
    def update_message(self): # 修改
        id=input('请输入要修改的学生的学号：')
        for i,a in enumerate(self.stu_list):
            if id==a[1]:
                message=input('请输入修改后的学生信息（班级 学号 姓名 分数）：')
                self.stu_list[i]=message.split()
                with open(r'E:/应用程序/Python/a-PythonProject/notefile/python_score.txt','w',encoding='utf-8') as f2:
                    for a in self.stu_list:
                        f2.write(a[0]+' '+a[1]+' '+a[2]+' '+a[3])
                        f2.write('\n')
                print('修改信息成功！')
                return 
        print('不存在此学号！')
    def search_message(self):# 查询
        id=input('请输入要查询的学生的学号：')
        for i,a in enumerate(self.stu_list):
            if id==a[1]:
                print('学生信息如下：')
                print(self.stu_list[i][0]+' '+self.stu_list[i][1]+' '+self.stu_list[i][2]+' '+self.stu_list[i][3])
                return 
        print('不存在此学号！')

    def print_message(self):  #打印
        print('学生信息如下(班级、学号、姓名、分数)：')
        for a in self.stu_list:
            print(a[0]+' '+a[1]+' '+a[2]+' '+a[3])
    
    @staticmethod
    def menufunc():
        while 1:
            os.system('cls')
            print('1.添加学生信息\n2.删除学生信息\n3.修改学生信息\n4.查询学生信息\n5.显示学生信息\n0.退出')
            try:
                choice=int(input('请输入功能选项：'))
            except Exception as e1:
                print(e1)
                os.system('pause')
                continue
            if choice>=0 and choice <=5:
                return choice
            else:
                print('输入有误！')
                os.system('pause')

manager=manage_student()
while 1:
    choice=manage_student.menufunc()
    if choice==1:
        manager.enter_message()
    elif choice==2:
        manager.delete_message()
    elif choice==3:
        manager.update_message()
    elif choice==4:
        manager.search_message()
    elif choice==5:
        manager.print_message()
    elif choice==0:
        sys.exit(0)
    os.system('pause')
