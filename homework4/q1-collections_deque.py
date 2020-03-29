# -*- encoding: utf-8 -*-
'''
@File : que1.py
@Time : 2020/03/28 15:59:47
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
定义一个10个元素的列表，通过列表自带的函数，
实现元素在尾部插入和头部插入并记录程序运行的时间；
用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
'''
from collections import deque
from datetime import datetime

list1=list(range(1,1111111))
q=deque(list1)
time1=datetime.now()
list1.insert(0,0)
list1.append(11)
time2=datetime.now()
print(time1,time2)
print('list函数实现时的时间差：{}s'.format((time2-time1).total_seconds()))
time3=datetime.now()
q.appendleft(0)
q.append(11)
time4=datetime.now()
print(time3,time4)
print('deque实现时的时间差：{}s'.format((time4-time3).total_seconds()))
