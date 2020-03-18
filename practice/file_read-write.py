# -*- encoding: utf-8 -*-
'''
@File : 1.17-prac4.py
@Time : 2020/03/18 19:39:13
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
list1=[]
str=""
print("文件读取内容如下：")
with open(r"Pcode\text1\ta.txt",'r',encoding="utf-8") as f1:  #读取文件
    for line in f1.readlines():
        print(line.strip())
        str=str+line
        list2=line.strip().split(" ")
        list3=[]
        for a in list2:
            if(a!=""):
                list3.append(a)
        list1.append(list3)
list1.sort(key=lambda p:p[2],reverse=True)
print("排序后输出：")
for a in list1:
    print('{}  {}  {}'.format(a[0],a[1],a[2]))
with open(r"Pypractice\wo.txt",'w',encoding='utf-8') as f2:  #写入文件
            f2.write(str)

