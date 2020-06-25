# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2020/5/18 21:16
# Tool ：PyCharm

import os

DIALECT = 'mysql'             # mysql数据库
DRIVER = 'mysqlconnector'
USERNAME = 'root'              # root用户
PASSWORD = 'wangyi200801'      # 密码
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format \
    (DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
