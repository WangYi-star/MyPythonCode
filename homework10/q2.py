# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2020/5/9 20:14
# Tool ：PyCharm
'''
设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）
（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；
'''
import pymysql
from datetime import datetime
import time
import sys

class Mes_Book:
    def __init__(self):
        try:
            password=input('输入密码：')
            self.db = pymysql.connect('localhost', 'root', password, 'test')
            self.cursor = self.db.cursor()
            print('数据库连接成功...')
            time.sleep(1)
        except Exception as e:
            print('数据库连接失败！')
            print(e)

    # 添加操作
    def insert_mes(self):
        id, name = input('请输入ID和姓名：（空格隔开）').split()
        content = input('请输入留言内容：')
        time_now = datetime.strftime(datetime.now().replace(microsecond=0), '%Y-%m-%d %H:%M:%S')
        sql = '''insert into mes_book (id,content,name,time_now,is_delete) values ('{}','{}','{}','{}',{})'''.\
            format(id, content, name, time_now, 0)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print('insert successfully!\n')
            time.sleep(1)
        except Exception as e:
            print('insert failed!')
            print(e)

    # 删除操作
    def delete_mes(self):
        id = input('请输入ID：')
        sql = '''delete from mes_book where id='{}' '''.format(id)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print('delete successfully!\n')
            time.sleep(1)
        except Exception as e:
            print('delete failed!')
            print(e)

    # 修改操作
    def update_mes(self):
        id = input('请输入要修改的ID：')
        content = input('请输入修改后的留言内容：')
        sql = '''update mes_book set content='{}' where id='{}' '''.format(content, id)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print('update successfully!\n')
            time.sleep(1)
        except Exception as e:
            print('update failed!')
            print(e)

    # 查询操作
    def select_mes(self):
        sql = 'select * from mes_book'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print('留言信息如下：')
        for mes in data:
            print(mes[0], mes[1], mes[2], mes[3], mes[4])
        print()
        time.sleep(1)

    def choice(self):
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

    def main(self):
        while True:
            ch = self.choice()
            if ch == 1:
                self.insert_mes()
            elif ch == 2:
                self.delete_mes()
            elif ch == 3:
                self.update_mes()
            elif ch == 4:
                self.select_mes()
            elif ch == 5:
                self.db.close()
                sys.exit(0)


if __name__ == '__main__':
    book = Mes_Book()
    book.main()


