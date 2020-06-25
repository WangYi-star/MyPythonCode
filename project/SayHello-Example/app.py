# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2020/5/19 11:45
# Tool ：PyCharm
from sayhello import app, db, bootstrap
from sayhello import model
from sayhello import commands
from sayhello import views


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')