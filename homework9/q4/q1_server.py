# -*- encoding: utf-8 -*-
'''
@File : q1.py
@Time : 2020/05/04 17:28:30
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

class server_class:
    def __init__(self):
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.users={}
        
    def s_listen(self):
        ip=socket.gethostname()
        try:
            self.s.bind((ip,9999))
        except Exception as e:
            print(e)
        self.s.listen(5)
        print("服务器已开启，等待连接...")
        print('在空白处输入exit并按enter键，关闭服务器。')
        self.s_accept()
        
    def s_accept(self):
        while True:
            sock,addr=self.s.accept()
            self.users[addr]=sock
            number=len(self.users)
            print('用户{}连接成功！现共有{}位用户。'.format(addr,number))
            Thread(target=self.client_thread,args=(sock,addr)).start()

        
    def client_thread(self,sock,addr):
        while True:
            try:
                data=sock.recv(4096).decode('utf-8')
                text='用户{}发来消息：{}'.format(addr,data)
                for client in self.users.values():
                    client.send(text.encode('utf-8'))
            except Exception as e:
                print('用户{}已经退出聊天！'.format(addr))
                self.users.pop(addr)
                break
            
    def close_server(self):
        for client in self.users.values():
            client.close()
        self.s.close()
        sys.exit(0)

if __name__=='__main__':
    server=server_class()
    server.s_listen()
    while True:
        cmd=input()
        if(cmd=='exit'):
            server.close_server()
        else:
            print('输入命令无效，请重新输入！')