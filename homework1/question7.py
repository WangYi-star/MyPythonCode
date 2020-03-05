# -*- encoding: utf-8 -*-
'''
@File : question7.py
@Time : 2020/03/05 17:33:10
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
print("9*9乘法表如下：")
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={:<2}  '.format(j,i,j*i),end="")  #对齐方式
    print()
#format:{ [index][ : [ [fill] align] [sign] [#] [width] [.precision] [type] ] }