# -*- encoding: utf-8 -*-
'''
@File : q3_client.py
@Time : 2020/05/03 16:57:29
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
'''
# # 客户端
# import socket

# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# ip=socket.gethostname()
# while True:
#     text=input('客户端：')
#     s.sendto(text.encode('utf-8'),(ip,9999))
#     data=s.recv(1024)
#     print('服务器端：\n'+data.decode('utf-8'))

import socket
import threading

def s_recv(s):
    while True:
        data=s.recv(1024).decode('utf-8')
        print('服务器端：\n'+data)

def s_send(s,ip):
    while True:
        text=input()
        s.sendto(text.encode('utf-8'),(ip,9999))

if __name__=='__main__':
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ip=socket.gethostname()
    mes='客户端连接到服务器'
    s.sendto(mes.encode('utf-8'),(ip,9999))
    threading.Thread(target=s_send,args=(s,ip)).start()
    threading.Thread(target=s_recv,args=(s,)).start()
