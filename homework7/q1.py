# -*- encoding: utf-8 -*-
'''
@File : q1.py
@Time : 2020/04/18 19:14:34
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
import re

def main():
    path1=r'E:\应用程序\Python\b-Python Crawler\crawler-data\webspiderUrl.txt'
    path2=r'E:\应用程序\Python\b-Python Crawler\crawler-data\reurl.txt'
    try:
        with open(path1,'r',encoding='utf-8') as f1:
            with open(path2,'w',encoding='utf-8') as f2:
                while 1:
                    text=f1.readline()
                    if not text:
                        break
                    print(text)
                    # ret=re.search(r'\'http://.*\'',text)
                    src = r'http://[^\';]*'  # 正则表达式匹配规则
                    imgre = re.compile(src)  # re.compile()，可以把正则表达式编译成一个正则表达式对象
                    imglist = re.findall(imgre, text)  # 读取html中包含imgre（正则表达式）的数据,imglist是包含了所有src元素的数组
                    # if ret:
                    #     f2.write(ret.group())
                    #     f2.write('\n')
                    for a in imglist:
                        f2.write(a)
                        f2.write('\n')
    except Exception as e1:
        print(e1)

if __name__=='__main__':
    main()