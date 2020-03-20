# -*- encoding: utf-8 -*-
'''
@File : question4.py
@Time : 2020/03/20 15:57:09
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
将当前img目录所有以.png结尾的后缀名改为.jpg.
'''
import os
try:
    files=os.listdir(r'img')
    os.chdir(os.getcwd()+"\img")
except Exception as ex:
    print(ex)
for filename in files:
    part=os.path.splitext(filename)
    if(part[1]=='.png'):
        newname=part[0]+'.jpg'
        os.rename(filename,newname)
