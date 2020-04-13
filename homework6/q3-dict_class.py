# -*- encoding: utf-8 -*-
'''
@File : q3.py
@Time : 2020/04/10 00:18:27
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key
del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
get_dict(key)
3 返回键组成的列表：返回类型;(list)
get_key()
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
update_dict({要合并的字典})
'''
class dictclass:
    def __init__(self,mydict):
        self.mydict=mydict
    
    def del_dict(self,key):
        del self.mydict[key]

    def get_dict(self,key):
        if key in self.mydict.keys():
            return self.mydict[key]
        else:
            return key+' not found'

    def get_key(self):
        return list(self.mydict.keys())

    def update_dict(self,updict):
        for k in updict.keys():
            self.mydict[k]=updict[k]
        return list(self.mydict.values())

    def printdict(self):
        print('操作后的字典：',self.mydict)

mydict={'姓名':'张三','年龄':20,'性别':'男'}
updict={'英语':85,'数学':78,'语文':82}
dict1=dictclass(mydict)
dict1.del_dict('性别')
dict1.printdict()
print(dict1.get_dict('性别'))
print(dict1.get_dict('姓名'))
print('keys:',dict1.get_key())
print(dict1.update_dict(updict))
dict1.printdict()

