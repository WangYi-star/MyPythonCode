# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2020/5/9 20:14
# Tool ：PyCharm
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import time
import sys

try:
    engine = create_engine('mysql+mysqlconnector://root:wangyi200801@localhost:3306/test')
    DBSession = sessionmaker(bind=engine)
    print('数据库连接成功...')
    session = DBSession()
    Base = declarative_base()
except Exception as e:
    print(e)

class Book(Base):
    __tablename__ = 'mes_book'
    id = Column(String(255), primary_key=True)
    content = Column(String(255))
    name = Column(String(20))
    time_now = Column(String(50))
    is_delete = Column(Integer)

# 添加操作
def insert_mes():
    b_id, b_name = input("请输入ID和姓名：（空格隔开）").split()
    b_content = input('请输入留言信息：')
    b_time_now = datetime.strftime(datetime.now().replace(microsecond=0),'%Y-%m-%d %H:%M:%S')
    b = Book(id=b_id, name=b_name, content=b_content, time_now=b_time_now, is_delete=0)
    try:
        session.add(b)
        session.commit()
        print('insert successfully!\n')
    except Exception as e:
        print('insert failed!')
        print(e)

# 删除操作
def delete_mes():
    try:
        b_id = input('请输入要删除的ID：')
        query1 = session.query(Book).filter(Book.id == b_id).first()
        session.delete(query1)
        session.commit()
        print('delete successfully!\n')
    except Exception as e:
        print('delete failed!')
        print(e)

# 修改操作
def update_mes():
    try:
        b_id = input('请输入要修改的ID：')
        b_content=input('请输入修改后的留言信息：')
        query1=session.query(Book).filter(Book.id == b_id).one()
        query1.content = b_content
        session.commit()
        print('update successfully!\n')
    except Exception as e:
        print('update failed!')
        print(e)

# 查询操作
def select_mes():
    try:
        query1 = session.query(Book).all()
        print('留言信息如下：')
        for data in query1:
            print(data.id, data.name, data.content, data.time_now, data.is_delete)
        print()
    except Exception as e:
        print(e)

def choice():
    print('1.添加留言信息\n2.删除留言信息\n3.修改留言信息（根据ID修改）\n4.显示留言信息\n5.退出\n')
    print('请输入选项：')
    while True:
        try:
            ch = int(input())
            if isinstance(ch,int) and ch>=1 and ch<=5:
                return ch
            else:
                raise Exception
        except:
            print('输入1-5的整数，请重新输入...')

if __name__ == '__main__':
    while True:
        time.sleep(1)
        ch = choice()
        if ch == 1:
            insert_mes()
        elif ch == 2:
            delete_mes()
        elif ch == 3:
            update_mes()
        elif ch == 4:
            select_mes()
        elif ch == 5:
            session.close()
            sys.exit(0)