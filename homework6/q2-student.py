# -*- encoding: utf-8 -*-
'''
@File : q2.py
@Time : 2020/04/10 00:05:51
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
定义一个学生Student类。有下面的类属性：
1 姓名 name
2 年龄 age
3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下:
'''

class Student:
    def __init__(self,name,age,score):
        self.__name=name
        self.__age=age
        self.score=score
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_course(self):
        # self.score.sort(key=lambda p:p,reverse=True)
        # return self.score[0]
        return max(self.score)

print('stu1:')
stu1=Student('张三',20,[64,75,88])
print('姓名：',stu1.get_name())
print('年龄：',stu1.get_age())
print('最高分：',stu1.get_course())
print('stu2:')
stu2=Student('李四',19,[52,86,63])
print('姓名：',stu2.get_name())
print('年龄：',stu2.get_age())
print('最高分：',stu2.get_course())