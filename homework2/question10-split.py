# -*- encoding: utf-8 -*-
'''
@File : question10.py
@Time : 2020/03/09 17:46:37
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)
'''
def calculate(str):
    if str.find("+")!=-1:
        i=str.index("+")
        print("%.2f" % (float(str[0:i])+float(str[i+1:])))
    elif str.find("-")!=-1:
        i=str.index("-")
        print("%.2f" % (float(str[0:i])-float(str[i+1:])))
    elif str.find("*")!=-1:
        i=str.index("*")
        print("%.2f" % (float(str[0:i])*float(str[i+1:])))
    elif str.find("/")!=-1:
        i=str.index("/")
        if(float(str[i+1:])==0):
            print("除数不能为0！")
        else:
            print("%.2f" % (float(str[0:i])/float(str[i+1:])))

str=input("输入两个数的运算：")
calculate(str)
