# -*- encoding: utf-8 -*-
'''
@File : q2.py
@Time : 2020/05/03 16:21:40
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
 编写一个接收数据的网络程序，
 由“网络调试工具”发送数据，你的程序接收数据并打印输出；
'''

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip=input('请输入ip地址：')
sock=int(input('请输入端口：'))
s.bind((ip,sock))
print('Bind UDP on 9999...')
while True:
    data,addr=s.recvfrom(1024)
    print('Received from {}:'.format(addr))
    print(data)