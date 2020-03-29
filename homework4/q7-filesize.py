# -*- encoding: utf-8 -*-
'''
@File : q7.py
@Time : 2020/03/29 00:03:34
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
使用python代码统计一个文件夹中所有文件的总大小
'''
import os
def solve(dpath):
    if not os.listdir(dpath):
        return 0
    else:
        sum=0
        for file in os.listdir(dpath):
            if os.path.isfile(os.path.join(dpath,file)):
                sum=sum+os.path.getsize(os.path.join(dpath,file))
            else:
                sum=sum+solve(os.path.join(dpath,file))
        return sum

dpath=input('请输入文件夹的地址：')
print('文件夹总大小：{}字节'.format(solve(dpath)))