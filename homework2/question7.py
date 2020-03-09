# -*- encoding: utf-8 -*-
'''
@File : question7.py
@Time : 2020/03/09 16:54:12
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;  
'''

def solve_score(a):
    for i in a:
        if(i>=90):
            print('{}  A'.format(i))
        elif i>=80 and i<90:
            print('{}  B'.format(i))
        elif i>=70 and i<80:
            print('{}  C'.format(i))
        else:
            print('{}  D'.format(i))

import random
a=[random.randint(50,100) for i in range(20)]
print("学生成绩：")
for i in a:
    print(i,end=" ")
print()
print("成绩等级：")
solve_score(a)