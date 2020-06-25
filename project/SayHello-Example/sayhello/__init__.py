# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2020/5/18 21:12
# Tool ：PyCharm

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask('sayhello', static_folder='static')
app.config.from_pyfile('config.py')

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
