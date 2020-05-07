# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2020/5/6 22:14
# Tool ：PyCharm
import pymysql
from datetime import datetime
import time
import sys

class mes_table:
    def __init__(self):
        # password=input('password:')
        self.db=pymysql.connect('localhost','root','wangyi200801','test')
        self.cursor=self.db.cursor()

    def create_table(self):
        try:
            self.cursor.execute('drop table if exists Mes_Board')
            self.cursor.execute('create table Mes_Board (id varchar(20),topic varchar(20),name varchar (20),time varchar (30))')
            print('create table successfullly...')
            time.sleep(1)
        except Exception as e:
            print(e)
    def insert_table(self):
        id,topic,name=input('请依次输入ID、留言主题、留言人(空格隔开):').split()
        t=datetime.now().replace(microsecond=0)
        time_now=t.strftime('%Y-%m-%d %H:%M:%S')
        sql='''insert into Mes_Board (id,topic,name,time) values ('%s','%s','%s','%s')''' % (id,topic,name,time_now)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print('insert successfully!')
            time.sleep(1)
        except Exception as e:
            print(e)

    def delete_table(self):
        id=input('请输入ID（根据ID删除）:')
        sql='''delete from Mes_Board where id='{}' '''.format(id)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print('delete successfully!')
            time.sleep(1)
        except Exception as e:
            print(e)

    def update_table(self):
        id = input('请输入ID（根据ID修改）:')
        topic=input('请输入修改后的留言主题：')
        sql='''update Mes_Board set topic='{}' where id ='{}' '''.format(topic,id)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print('update successfully!')
            time.sleep(1)
        except Exception as e:
            print(e)

    def select_talbe(self):
        print('留言信息如下：')
        self.cursor.execute('select * from Mes_Board')
        data=self.cursor.fetchall()
        for a in data:
            print(a[0],a[1],a[2],a[3])
        time.sleep(1)

    def choice(self):
        while True:
            print('1、添加留言板信息\n2、删除留言板信息\n3、修改留言板主题信息\n4、显示留言板信息\n5、退出')
            try:
                ch=int(input('请输入选项：（1-5）'))
                if ch<1 or ch>5:
                    raise Exception
                return ch
            except Exception:
                print('输入有误，请输入1-5的整数！！！')
                continue

    def main(self):
        while True:
            ch = self.choice()
            if ch == 1:
                self.insert_table()
            elif ch == 2:
                self.delete_table()
            elif ch == 3:
                self.update_table()
            elif ch == 4:
                self.select_talbe()
            else:
                self.db.close()
                sys.exit(0)

if __name__=='__main__':
    mes=mes_table()
    mes.create_table()
    mes.main()