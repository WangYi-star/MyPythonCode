# -*- encoding: utf-8 -*-
'''
@File : q2.py
@Time : 2020/05/04 18:02:24
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 多人聊天室
import socket
from threading import Thread
import sys


def recv_mes(s):
    print('连接成功！现在可以接收消息！')
    while True:
        try:
            text=s.recv(4096)
            print(text.decode('utf-8'))
        except Exception as e:
            print(e)

def send_mes(s):
    print("连接成功！现在可以发送消息！")
    print("输入消息按回车来发送")
    print("输入exit来退出聊天")
    while True:
        mes=input()
        if mes=='exit':
            print('你退出了聊天！')
            s.close()
            break
        s.send(mes.encode('utf-8'))
    sys.exit(0)

if __name__=='__main__':
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr=(socket.gethostname(),9999)
    s.connect(addr)
    Thread(target=recv_mes,args=(s,)).start()
    Thread(target=send_mes,args=(s,)).start()

