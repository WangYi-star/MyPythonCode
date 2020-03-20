# -*- encoding: utf-8 -*-
'''
@File : question1.py
@Time : 2020/03/20 10:18:08
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
写一个程序，读取键盘输入的任意行文字信息，
当输入空行时结束输入，将读入的字符串存于列表;
然后将列表里面的内容写入到文件input.txt中；
'''

list=[]
print("请输入任意行文字信息（输入空行是结束）：")
while 1:
    str=input()
    if(str==" "):
        break
    list.append(str)
print(list)
try:
    with open(r".\notefile\input.txt",'w',encoding='utf-8') as f1:
        for a in list:
            f1.write(a)
            f1.write('\n')
except FileNotFoundError as fnot:
    print(fnot)
