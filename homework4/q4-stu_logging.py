# -*- encoding: utf-8 -*-
'''
@File : q4.py
@Time : 2020/03/28 20:33:16
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
5个同学的姓名,账号和密码(加密后的),保存在一个文件上;  
系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）; 
如果都正确,打印提示, 您登录成功(失败);
'''

import hashlib
stu_list=[]
stu_dict={}
with open(r'notefile/stu_message.txt','r',encoding='utf-8') as f1:
    while True:
        text=f1.readline()
        if not text:
            break
        else:
            text_list=text.strip().split(" ")
            stu_list.append(text_list)
            if(text_list[0] in stu_dict.keys()):
                stu_dict[text_list[0]].append(text_list[1])
            else:
                mlist=[]
                mlist.append(text_list[1])
                stu_dict[text_list[0]]=mlist
name=input('请输入登录同学姓名：')
if name in stu_dict.keys():       #姓名存在
    account=input('请输入账号：')
    if account in stu_dict[name]:     #账号存在
        password=input('请输入密码：')
        md5=hashlib.md5()
        md5.update(password.encode('utf-8'))
        list_one=[name,account,md5.hexdigest()]
        if list_one in stu_list:
            print('登陆成功！')
        else:
            print('密码不正确！')
    else:
        print('账号不存在！')
else:
    print('不存在次姓名！')

