# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2020/4/19 15:14
# Tool ：PyCharm

from bs4 import BeautifulSoup
import requests
import re
import os

url='http://www.python3.vip/doc/prac/python/0001/'

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) \
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'
}

r=requests.get(url,headers=headers).content.decode('utf-8')
soup=BeautifulSoup(r,'html.parser')
re_ul=soup.find(class_='nav__items')
re_a=re_ul.find_all('a')
list_href=[]
for a in re_a:
	list_href.append(a.attrs['href'])

path=r'E:\应用程序\Python\b-Python Crawler\crawler-data'
with open(os.path.join(path,'prc-python.txt'),'w',encoding='utf-8')as f1:
	for x in list_href:
		try:
			test = requests.get(x, headers=headers).content.decode('utf-8')
			soup_text = BeautifulSoup(test, 'html.parser')
			title = soup_text.find(class_='page__inner-wrap').find('header').text
			f1.write('\n*****************************************************************\n'+title.strip()+'\n')
			content = soup_text.find(class_='content').text.strip()
			f1.write(content+'\n')
		except Exception as e1:
			print(e1)

# 			p_list = soup_text.find(class_='content').find_all('p', {'class': None, 'target': None, 'name': None})
# 			for a in p_list:
# 				if a.get_text().strip()!='':
# 					f1.write(a.get_text().strip()+'\n')
# 			tm_list=soup_text.find(class_='content').find_all('h2',{'id':re.compile('答案')})
# 			an_list=soup_text.find(class_='content').find_all('pre',{'class':'highlight'})
# 			for i in range(len(tm_list)):
# 				f1.write('\n'+tm_list[i].text.strip()+"\n")
# 				f1.write(an_list[i].text.strip()+'\n')


