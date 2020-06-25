# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2020/5/19 10:49
# Tool ：PyCharm

from sayhello import app, db
from sayhello.model import Message
from faker import Faker

try:
    db.create_all()
except Exception as e:
    print(e)

# 生成数据，初始化数据库
fake = Faker()
for i in range(40):
    message = Message(
        name=fake.name(),
        body=fake.sentence(),
        timestamp=fake.date_time_this_year()
    )
    db.session.add(message)
db.session.commit()
