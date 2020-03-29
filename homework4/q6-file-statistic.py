# -*- encoding: utf-8 -*-
'''
@File : q6.py
@Time : 2020/03/28 20:53:48
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，
如果是文件，显示大小; 输出格式效果如下:
    名称         日期                   类型（文件夹或者 文件）       大小
'''
import os
from datetime import datetime
def solve(dpath):
    filelist=[]
    list1=os.listdir(dpath)
    for file in list1:
        dict={}
        if(os.path.isfile(os.path.join(dpath,file))):
            dict['名称']=file
            chdate=datetime.fromtimestamp(os.path.getmtime(os.path.join(dpath,file)))
            dict['日期']=chdate.strftime('%Y-%m-%d %H:%M:%S')
            dict['类型']='文件'
            dict['大小']=os.path.getsize(os.path.join(dpath,file))
        else:
            dict['名称']=file
            chdate=datetime.fromtimestamp(os.path.getmtime(os.path.join(dpath,file)))
            dict['日期']=chdate.strftime('%Y-%m-%d %H:%M:%S')
            dict['类型']='文件夹'
            dict['大小']=""
        filelist.append(dict)
    print('{:<22}{:<20}{:<8}{:<4}'.format('名称','修改日期','类型','大小(字节)'))
    for a in filelist:
        print('{:<24}{:<24}{:<8}{:<4}'.format(a['名称'],a['日期'],a['类型'],a['大小']))

dpath=input('请输入绝对路径：')
solve(dpath)