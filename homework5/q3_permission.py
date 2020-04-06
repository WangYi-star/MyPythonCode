# -*- encoding: utf-8 -*-
'''
@File : q3_permission.py
@Time : 2020/04/06 18:07:42
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）
'''
import sys
def permission(func):
    def mainfunc(*arg,**kw):
        account=input('请输入账号：')
        if(account=='python'):
            password=input('请输入密码：')
            if(password=='000111'):
                return func(*arg,**kw)
            else:
                print('密码不正确！')
                sys.exit(0)
        else:
            print('账号不存在！')
            sys.exit(0)
    return mainfunc

@permission
def sum(x,y):
    print(x+y)

sum(12,15)