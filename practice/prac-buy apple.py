# -*- encoding: utf-8 -*-
'''
@File : prac1.py
@Time : 2020/03/04 09:16:21
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#提示输入需要购买的苹果的重量(斤),然后提示输入每斤的价格,
#请计算应支付的总价,并打印提示输出;

'''list1=[12,45,1,48,12,455,78,21,56,66]
for x in list1:
    if(x%2==0):
        print(x)
list2=list(range(5))
print(list2)
'''
a=int(input("请输入苹果重量："))
b=int(input("请输入苹果单价："))
def price(a,b):
    print('苹果总价：{}元'.format(a*b))
price(a,b)
