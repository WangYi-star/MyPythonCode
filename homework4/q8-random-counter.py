# -*- encoding: utf-8 -*-
'''
@File : q8.py
@Time : 2020/03/29 00:18:47
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
1） 生成一个大文件ip.txt,要求1200行，
    每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip
'''
import random
from collections import Counter

iplist=['172.25.254.'+str(random.randint(1,254)) for i in range(1200)]
with open(r'notefile/ip.txt','w') as f1:
    for a in iplist:
        f1.write(a)
        f1.write('\n')

c=Counter()
wlist=[]
with open(r'notefile/ip.txt','r') as f2:
    while True:
        text=f2.readline()
        if not text:
            break
        else:
            wlist.append(text.strip())
#for a in wlist:
 #   c[a]=c[a]+1
c.update(wlist)
print('出现频率排前十的ip:')
for a in c.most_common(10):
    print('ip:{:<18}频率：{:<4}'.format(a[0],a[1]))

