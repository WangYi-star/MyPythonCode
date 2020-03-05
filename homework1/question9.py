# -*- encoding: utf-8 -*-
'''
@File : question.py
@Time : 2020/03/05 19:05:52
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
print("猜字游戏：0-50(五次机会)")
for a in range(0,5):
    b=int(input("\n请输入数字："))
    print(b)
    if b==10:
        print("猜字成功！")
        break
    else:
        print("猜字失败！")
        print('你还有{}次机会。'.format(4-a))