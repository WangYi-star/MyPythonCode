# -*- encoding: utf-8 -*-
'''
@File : q4.py
@Time : 2020/04/06 18:31:08
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
编写装饰器来实现，对目标函数进行装饰，分3种情况：
目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
     三个目标函数分别为：
     A 打印输出20000之内的素数；
     B 计算整数2-10000之间的素数的个数；
     C 计算整数2-M之间的素数的个数；
'''

def log(func):
    def mainfunc(*arg,**kw):
        print('call {}()'.format(func.__name__))
        re=func(*arg,**kw)
        if re:
            print(re)
        #return func(*arg,**kw)
    return mainfunc


@log
def funcA():
    for a in range(2,20000):
        flag=1
        for i in range(2,a):
            if a%i==0:
                flag=0
                break
        if flag==1:
            print(a,end=' ')
    print('\n')

funcA()


@log
def funcB(x,y):
    sum=0
    for a in range(x,y+1):
        flag=1
        for i in range(2,a):
            if a%i==0:
                flag=0
                break
        if flag==1:
            sum=sum+1
    print(sum)

funcB(2,10000)


@log
def funcC():
    sum=0
    for a in range(2,10000):
        flag=1
        for i in range(2,a):
            if a%i==0:
                flag=0
                break
        if flag==1:
            sum=sum+1
    return sum

funcC()
