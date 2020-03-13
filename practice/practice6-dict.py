# -*- encoding: utf-8 -*-
'''
@File : practice6-dict.py
@Time : 2020/02/28 20:22:47
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
dict1={"id":120181080608,"name":"WY","class":1802,"age":20}
print(dict1["id"])
print(dict1["name"])
print(dict1)
dict2={"stu1":("001","A"),"sty2":("002","B"),"stu3":("003","C"),"stu4":("004","D"),"stu5":("005","E")}
print(dict2["stu1"])
print(dict2["stu1"][0])
print(dict2)
'''
#字典元素修改
dict={"A":"aa","B":"bb","C":"cc"}
print(dict)
dict["D"]="dd"
print(dict)
dict["A"]="aaa"
print(dict)
del dict["A"]
print(dict)
print(str(dict))