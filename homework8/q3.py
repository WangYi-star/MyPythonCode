# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2020/4/27 22:48
# Tool ：PyCharm
'''
计算1～100000之间所有素数的个数， 要求如下:
- 编写函数判断一个数字是否为素数，然后统计素数的个数；
-对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
-对比2：对比开启4个多进程和开启10个多进程两种方法的速度。
'''
from multiprocessing import Process,Queue
import time

def work(q1,q2):
    count=0
    while not q1.empty():
        t = q1.get()
        if t == 2:
            count+=1
        elif t > 2:
            flag = 1
            for i in range(2, t):
                if t % i == 0:
                    flag = 0
                    break
            if flag == 1:
                count+=1
    q2.put(count)

if __name__=='__main__':
    q1=Queue()
    for i in range(1,100001):
        q1.put(i)
    q2=Queue()
    count = 0
    # 不使用多进程
    # start=time.time()
    # work(q1,q2)
    # while not q2.empty():
    #     count=count+q2.get()
    # print('素数个数：',count)
    # end=time.time()
    # print('用时：{}s'.format(end-start))

    # 4个多进程
    # start=time.time()
    # p1=Process(target=work,args=(q1,q2))
    # p1.start()
    # p2=Process(target=work,args=(q1,q2))
    # p2.start()
    # p3=Process(target=work,args=(q1,q2))
    # p3.start()
    # p4=Process(target=work,args=(q1,q2))
    # p4.start()
    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    # while not q2.empty():
    #     count=count+q2.get()
    # print('素数个数：',count)
    # end=time.time()
    # print('用时：{}s'.format(end-start))


    # 10个多进程
    start=time.time()
    p1=Process(target=work,args=(q1,q2))
    p1.start()
    p2=Process(target=work,args=(q1,q2))
    p2.start()
    p3=Process(target=work,args=(q1,q2))
    p3.start()
    p4=Process(target=work,args=(q1,q2))
    p4.start()
    p5= Process(target=work, args=(q1, q2))
    p5.start()
    p6 = Process(target=work, args=(q1, q2))
    p6.start()
    p7 = Process(target=work, args=(q1, q2))
    p7.start()
    p8 = Process(target=work, args=(q1, q2))
    p8.start()
    p9 = Process(target=work, args=(q1, q2))
    p9.start()
    p10 = Process(target=work, args=(q1, q2))
    p10.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()
    while not q2.empty():
        count=count+q2.get()
    print('素数个数：',count)
    end=time.time()
    print('用时：{}s'.format(end-start))