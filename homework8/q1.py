# -*- encoding: utf-8 -*-
'''
@File : q1.py
@Time : 2020/04/27 09:52:06
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
  有100个同学的分数：数据请用随机函数生成；
     A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
     B  利用线程池来实现；

'''

from random import randint
from threading import Thread
import queue,time

def work1():
  global it
  for i in range(20):
      try:
          print(next(it))
      except StopIteration:
          return

class ThreadPool(object):
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self._q = queue.Queue(self.maxsize)
        for i in range(self.maxsize):
            self._q.put(Thread)
 
    def getThread(self):
        return self._q.get()
 
    def addThread(self):
        self._q.put(Thread)

def work2(p):
    global it
    for i in range(20):
        try:

            print(next(it))
        except StopIteration:
            return 
    p.addThread()
 
          
if __name__=='__main__':
    score_list=[randint(20,100) for a in range(100)]
    it=iter(score_list)

    print('多线程输出：')
    for i in range(5):
          t=Thread(target=work1)
          t.start()
    time.sleep(2)
    
    print('线程池：')
    it=iter(score_list)
    pool = ThreadPool(3)
    for i in range(5):
        t = pool.getThread()
        a = t(target = work2,args=(pool,))
        a.start()

