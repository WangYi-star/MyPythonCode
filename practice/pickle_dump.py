# -*- encoding: utf-8 -*-
'''
@File : pickle.py
@Time : 2020/03/18 21:05:25
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

import pickle,pprint
dict={"1":("110","a",18),"2":("111","b",19),"3":("112","c",20),\
    "4":("113","d",20),"5":("114","e",20)}


output = open('.\Pypractice\wo.txt', 'wb')
pickle.dump(dict,output)
output.close()

file = open('.\Pypractice\wo.txt', 'rb')
str=pickle.load(file)
pprint.pprint(str)
file.close()