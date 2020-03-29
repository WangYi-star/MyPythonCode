# -*- encoding: utf-8 -*-
'''
@File : q3.py
@Time : 2020/03/28 20:03:44
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
        Tom   admin   XXXXX
        Jack   root      XXXXX
'''
import hashlib

with open(r'notefile/stu_message.txt','w',encoding='utf-8') as f1:
        print('请依次输入五个同学的姓名、账号、密码（例如：李四 wangwu 123456）：')
        for i in range(5):
            a,b,c=input().split(" ")
            md5 = hashlib.md5()
            md5.update(c.encode('utf-8'))
            mess=a+" "+b+" "+md5.hexdigest()
            f1.write(mess)
            f1.write('\n')
