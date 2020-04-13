# -*- encoding: utf-8 -*-
'''
@File : fight_dog.py
@Time : 2020/04/10 19:29:39
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

import sys

class dog:
    def __init__(self):
        self.aggressive = 15
        self.blood = 80

    def be_attacked(self):
        self.blood = self.blood - 10
        self.aggressive = self.aggressive - 3
        if self.blood<0:
            self.blood=0
        if self.aggressive<0:
            self.aggressive=0

    def dok(self):  # 可攻击
        if (self.blood>0 and self.aggressive>0):
            return True
        return False