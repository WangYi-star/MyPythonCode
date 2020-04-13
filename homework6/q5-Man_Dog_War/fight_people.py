# -*- encoding: utf-8 -*-
'''
@File : fight_people.py
@Time : 2020/04/10 19:18:19
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

import sys

class people:
    def __init__(self):
        self.aggressive = 10
        self.blood = 100

    def be_attacked(self):
        self.blood = self.blood - 15
        self.aggressive = self.aggressive - 2
        if self.blood<0:
            self.blood=0
        if self.aggressive<0:
            self.aggressive=0

    def pok(self):
        if (self.blood>0 and self.aggressive>0):  # 有战斗力
            return True
        return False