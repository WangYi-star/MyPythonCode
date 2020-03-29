# -*- encoding: utf-8 -*-
'''
@File : q2.py
@Time : 2020/03/28 16:41:50
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
定义一个函数，判断一个输入的日期，是当年的第几周，周几？  将程序改写一下，
能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；
'''
from datetime import *

def judgeweek(str1):  #字符串（当年）  字符串（日期）
    ny=datetime.now().year
    date0=datetime(ny,1,1)

    date1=datetime.strptime(str(ny)+'-'+str1,'%Y-%m-%d') #输入的日期
    days=(date1-date0).days
    print('此日期是当年的第{}周的周{}'.format(int(1+days/7),date1.isoweekday()))

def schoolweek(str1):  #字符串（当年）  字符串（日期）
    ny=datetime.now().year
    date0=datetime(ny,2,17)
    date1=datetime.strptime(str(ny)+'-'+str1,'%Y-%m-%d') #输入的日期
    days=(date1-date0).days
    print('此日期是校历的第{}周的周{}'.format(int(1+days/7),date1.isoweekday()))

str1=input('请输入日期：（列如：2-22）')
judgeweek(str1)
schoolweek(str1)