# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2020/4/28 0:01
# Tool ：PyCharm
'''
编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息；
'''
from multiprocessing import Process,Queue
import time
def received(q):
    while 1:
        if not q.empty():
            print('接收消息：\n',q.get())
        time.sleep(0.2)

if __name__=='__main__':
    q=Queue()
    rece=Process(target=received,args=(q,))
    rece.start()
    while 1:
        text=input('输入消息：')
        q.put(text)
        time.sleep(0.2)