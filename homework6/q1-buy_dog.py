# -*- encoding: utf-8 -*-
'''
@File : q1.py
@Time : 2020/04/09 23:29:07
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
定义一个狗类,里面有一个列表成员变量(列表的元素是字典), 
分别记录了 3种颜色的狗的颜色, 数量,和价格;
实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;
'''

import sys
class dog:
    dog_list=[{'颜色':['黑色','黄色','白色']},{'数量':[14,18,9]},{'价格':[200,210,240]}]
    @classmethod
    def buy_dog(cls,colour,num):
        if colour=='黑色':
            cls.dog_list[1]['数量'][0]=cls.dog_list[1]['数量'][0]-num
        elif colour=='黄色':
            cls.dog_list[1]['数量'][1]=cls.dog_list[1]['数量'][1]-num
        elif colour=='白色':
            cls.dog_list[1]['数量'][2]=cls.dog_list[1]['数量'][2]-num        

    @staticmethod
    def printdog():
        print('剩余各类狗的数量：')
        for i in range(3):
            print(dog.dog_list[0]['颜色'][i],dog.dog_list[1]['数量'][i])    

dog.printdog()
while 1:
    bdog1=input('请输入狗的颜色和购买数量：').split()
    dog.buy_dog(bdog1[0],int(bdog1[1]))
    dog.printdog()
    judge=input('是否继续购买？（y/n）')
    if judge=='n':
        sys.exit(0)
