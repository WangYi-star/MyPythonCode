# -*- encoding: utf-8 -*-
'''
@File : practice3-swing.py
@Time : 2020/02/28 19:36:17
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
str="center find count len max min  replace"
if "find" in str:
    print("\'find\'在str中！")
else:
    print("\'find\'不在str中！")
if str.find("find")!=-1:
    print("\'find\'在str中！")
else:
    print("\'find\'不在str中！")
print("将str中的\'max min\'替换为\'sum\':")
print(str.replace("max min","sum"))
print("str长：",end="")
print(len(str))