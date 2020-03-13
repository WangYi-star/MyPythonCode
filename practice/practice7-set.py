# -*- encoding: utf-8 -*-
'''
@File : practice7-set.py
@Time : 2020/02/28 20:43:38
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
set1={"a","b","c","d","e",1,2}
set2=set((1,2,3,4,5,"a","b"))
print(set1-set2)
print(set1 | set2)
print(set1&set2)
print(set1^set2)
print("增加：")
set1.add("f")
set2.update("d")
print(set1)
print(set2)
print("删除：")
set1.remove("f")
set1.discard("e")
set1.pop()
print(set1)
print("set2元素个数：")
print(len(set2))


