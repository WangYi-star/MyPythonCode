# -*- encoding: utf-8 -*-
'''
@File : q3.py
@Time : 2020/05/03 16:45:41
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
'''
 # 服务器端
# import socket

# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# ip=socket.gethostname()
# s.bind((ip,9999))
# while True:
#     data,addr=s.recvfrom(1024)
#     print('客户端：\n'+data.decode('utf-8'))
#     text=input('服务器端：')
#     s.sendto(text.encode('utf-8'),addr)

import socket
from threading import Thread

def receive():
    while True:
        data,addr=s.recvfrom(1024)
        print('客户端：\n'+data.decode('utf-8'))

def send(addr):
    while True:
        text=input()
        s.sendto(text.encode('utf-8'),addr)

if __name__=='__main__':
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ip=socket.gethostname()
    s.bind((ip,9999))
    data,addr=s.recvfrom(1024)
    print(data.decode('utf-8'))
    Thread(target=receive).start()
    Thread(target=send,args=(addr,)).start()
