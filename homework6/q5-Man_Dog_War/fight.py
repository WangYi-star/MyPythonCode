# -*- encoding: utf-8 -*-
'''
@File : q5.py
@Time : 2020/04/10 17:12:44
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
请写一个小游戏，人狗大站;  规则:
    1：2个角色，人和狗，游戏开始后，生成2个人，3条狗，人狗互相交替对战(注意,人只能打狗,  狗也只会咬人); 
        人的打击力为10;  初始化血为100;    狗的攻击力为 15; 初始化血为80;
    2：人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。血为0的话,表示死亡,退出游戏;
        人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2;  狗被打一次,攻击力降低3);
    3：对战规则: 
     A  随机决定,谁先开始攻击; 
     B  一方攻击完毕后, 另外一方再开始攻击;  攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
     C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
     提示：注意组织代码的方式；狗类用一个单独的py文件； 人用一个单独的py文件； 
     再写一个fight模块（也用类来组织；在这个模块中，导入人和狗模块中编写好的方法）
'''

import sys
import time
from random import randint
from fight_people import people
from fight_dog import dog

class fight:
    def __init__(self,pnum,dnum):
        self.p_list=[]       # 存放people
        self.d_list=[]      # 存放dog
        for i in range(pnum):
            self.p_list.append(people())
        for i in range(dnum):
            self.d_list.append((dog()))
        self.p_index=list(range(pnum))    # 活着的索引
        self.d_index=list(range(dnum))
        self.pf_index=list(range(pnum))   # 可攻击的索引
        self.df_index=list(range(dnum))
    def people_attack(self):          # 人攻击
        if len(self.pf_index)>0:             # 存在可攻击的人
            ran1=randint(0,len(self.pf_index)-1)    # 随机挑选一个人进行攻击
            # print('ran1:',ran1,self.pf_index[ran1])
            p=self.p_list[self.pf_index[ran1]]    # 被选中的攻击者
            ran2=randint(0,len(self.d_index)-1)     # 随机挑选一个被攻击的狗
            d=self.d_list[self.d_index[ran2]]     # 被选中的受攻击者
            print('******p{} fight d{}******'.format(self.pf_index[ran1],self.d_index[ran2]))
            (self.d_list[self.d_index[ran2]]).be_attacked()    # 进行攻击
            if (self.d_list[self.d_index[ran2]]).blood<=0:
                if self.d_index[ran2] in self.df_index:
                    set=self.df_index.index(self.d_index[ran2])
                    self.df_index.pop(set)
                self.d_index.pop(ran2)
            elif (self.d_list[self.d_index[ran2]]).aggressive<=0:
                if self.d_index[ran2] in self.df_index:
                    set = self.df_index.index(self.d_index[ran2])
                    self.df_index.pop(set)       # 攻击后的处理
            if len(self.d_index)==0:
                print('People Win!')
                sys.exit(0)
        else:
            print('people aggressive is 0')

    def dog_attack(self):
        if len(self.df_index)>0:
            ran1=randint(0,len(self.df_index)-1)
            d=self.d_list[self.df_index[ran1]] # 被选中的攻击者
            ran2=randint(0,len(self.p_index)-1)
            d=self.p_list[self.p_index[ran2]] # 受攻击者
            print('******d{} fight p{}******'.format(self.df_index[ran1],self.p_index[ran2]))
            (self.p_list[self.p_index[ran2]]).be_attacked()
            if(self.p_list[self.p_index[ran2]]).blood<=0:
                if self.p_index[ran2] in self.pf_index:
                    set = self.pf_index.index(self.p_index[ran2])
                    self.pf_index.pop(set)
                self.p_index.pop(ran2)
            elif (self.p_list[self.p_index[ran2]]).aggressive<=0:
                if self.p_index[ran2] in self.pf_index:
                    set = self.pf_index.index(self.p_index[ran2])
                    self.pf_index.pop(set)
            if len(self.p_index)==0:
                print('Dog Win')
                sys.exit(0)
        else:
            print('dog aggressive is 0')

    def print_state(self):
        print('people:(blood aggressive)')
        for i,a in enumerate(self.p_list):
            print('p'+str(i)+':',a.blood,a.aggressive,end='    ')
        print('\n')
        print('dog:(blood aggressive)')
        for i,a in enumerate(self.d_list):
            print('d'+str(i)+':',a.blood, a.aggressive, end='    ')
        print('\n')

num=input('请分别输入人、狗的数量：').split()
fighter1=fight(int(num[0]),int(num[1]))
time.sleep(1.5)
print('开始战斗！')
fighter1.print_state()
Round=1
while 1:
    time.sleep(1)
    print('第{}回合：'.format(Round))
    time.sleep(1)
    fighter1.people_attack()
    time.sleep(1)
    fighter1.print_state()
    time.sleep(1.5)
    fighter1.dog_attack()
    time.sleep(1)
    fighter1.print_state()
    time.sleep(1)
    Round=Round+1


