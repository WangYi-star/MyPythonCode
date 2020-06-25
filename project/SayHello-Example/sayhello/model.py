# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2020/5/18 21:24
# Tool ：PyCharm

from datetime import datetime

from sayhello import db

# 存储留言信息的表
class Message(db.Model):
    __tablename__ = 'mymess'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)

# 存储登录信息的表
class Login(db.Model):
    __tablename__ = 'login'
    username = db.Column(db.String(50, 'utf8_unicode_ci'), primary_key=True)
    password = db.Column(db.String(50, 'utf8_unicode_ci'), nullable=False)
