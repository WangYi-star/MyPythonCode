# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2020/5/9 16:31
# Tool ：PyCharm

from sqlalchemy import Column, String, create_engine, Enum, Integer, DECIMAL, Boolean,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import or_, and_


password=input('输入密码：')
engine = create_engine('mysql+mysqlconnector://root:'+password+'@localhost:3306/test')
DBSession = sessionmaker(bind=engine)
Base = declarative_base()
class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)
    height = Column(DECIMAL(5, 2))
    gender = Column(Enum('男', '女', '中性', '保密'))
    cls_id = Column(Integer)
    is_delete = Column(Boolean)

session = DBSession()

# 查询所有男生的姓名，年龄，所在班级名称；
def work1():
    query1 = session.query(Students.name, Students.age, Students.cls_id).filter(Students.gender == '男').all()
    # print(*query1)
    for data in query1:
        print(*data)
print('查询所有男生的姓名，年龄，所在班级名称:')
work1()
print('\n')

# 查询所有查询编号小于4或没被删除的学生；
def work2():
    query1=session.query(Students).filter(or_(Students.id<4, Students.is_delete==0)).all()
    for data in query1:
        print(data.id, data.name, data.age, data.height, data.gender, data.cls_id, data.is_delete)
print('查询所有查询编号小于4或没被删除的学生:')
work2()
print('\n')

# 查询姓黄并且“名”是一个字的学生；
def work3():
    query1=session.query(Students).filter(Students.name.like('黄_')).all()
    for data in query1:
        print(data.id, data.name, data.age, data.height, data.gender, data.cls_id, data.is_delete)
print('查询姓黄并且“名”是一个字的学生:')
work3()
print('\n')

# 查询编号是1或3或8的学生
def work4():
    query1=session.query(Students).filter(or_(Students.id==1,Students.id==3,Students.id==8)).all()
    for data in query1:
        print(data.id, data.name, data.age, data.height, data.gender, data.cls_id, data.is_delete)
print('查询编号是1或3或8的学生:')
work4()
print('\n')

# 查询编号为3至8的学生
def work5():
    query1=session.query(Students).filter(and_(Students.id>=3, Students.id<=8)).all()
    for data in query1:
        print(data.id, data.name, data.age, data.height, data.gender, data.cls_id, data.is_delete)
print('查询编号为3至8的学生:')
work5()
print('\n')

# 查询未删除男生信息，按年龄降序
def work6():
    query1=session.query(Students).filter(Students.is_delete==0).order_by(Students.age.desc()).all()
    for data in query1:
        print(data.id, data.name, data.age, data.height, data.gender, data.cls_id, data.is_delete)
print('查询未删除男生信息，按年龄降序:')
work6()
print('\n')

# 查询女生的总数
def work7():
    query1=session.query(func.count(Students.id)).filter(Students.gender == '女').scalar()
    print(query1)
print('查询女生的总数:')
work7()
print('\n')

# 查询学生的平均年龄
def work8():
    query1 = session.query(func.avg(Students.age)).scalar()
    print(query1)
print('查询学生的平均年龄:')
work8()
print('\n')

# 分别统计性别为男/女的人年龄平均值
def work9():
    query1=session.query(func.avg(Students.age)).filter(Students.gender=='男').scalar()
    print(query1)
    query2 = session.query(func.avg(Students.age)).filter(Students.gender == '女').scalar()
    print(query2)
print('分别统计性别为男/女的人年龄平均值:')
work9()
print('\n')

'''
⑩ 按照性别来进行人员分组如下显示（group by + group_concat()）；
        | 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖                                 |
	| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                        |
	| 中性   | 金星                                                       |
	| 保密   | 凤姐 
'''
def work10():
    # query1=session.query(Students.,func.count(Students.name)).group_by(Students.gender).all()
    # print(query1)
    query1=session.query(Students.gender, func.group_concat(Students.name)).group_by(Students.gender).all()
    for data in query1:
        print('{:6}{}'.format(data[0], data[1]))
print('按照性别来进行人员分组如下显示:')
work10()

session.close()