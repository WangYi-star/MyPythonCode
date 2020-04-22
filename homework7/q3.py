# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2020/4/18 23:30
# Tool ：PyCharm
import requests
import re
from urllib.parse import quote
from urllib import request
# import wget
# import subprocess
# import os

def gethtml(url):
    header= {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
    response=requests.get(url,headers=header)
    html = response.text
    return html

def getmp3url(html):
    src=r'sc-ad [^\']*\.mp3'
    mp3 = re.compile(src)
    mp3list = re.findall(mp3, html)
    mp3list=list(set(mp3list))
    for i in range(len(mp3list)):
        mp3list[i]='http://www.listeningexpress.com/studioclassroom/ad/'+quote(mp3list[i])
    for a in mp3list:
        print(a)
    return mp3list

def downloadmp3s(mp3list):
    path=r'E:\应用程序\Python\b-Python Crawler\crawler-data\MP32'
    # # cmd = 'wget %s %s' % (path, mp3list[0])
    # cmd="wget \"%s\" -c -T 10 -t 10 -O \"%s\"" % (mp3list[0], path)
    # # subprocess.call(cmd, shell=True)
    # os.system(cmd)
    x = 0
    for url in mp3list:
        request.urlretrieve(url, path+'\%s.mp3' %x)
        x += 1
        print('downloading: '+url,'\n')

    # x=0
    # path=r'E:\应用程序\Python\b-Python Crawler\crawler-data\MP32'
    # for url in mp3list:
    #     wget.download(url, out=path+r'\%s.mp3' %x)
    #     x += 1
    #     print('downloading: '+url,'\n')
    # wget.download(mp3list[0],out=path)


    # x=0
    # path = r'E:\应用程序\Python\b-Python Crawler\crawler-data\MP32'
    # for url in mp3list:
    #     cmd = 'wget --no-check-certificate -O %s %s ' % (path+r'\%s.mp3' %x, url)
    #     subprocess.call(cmd, shell=True)
    #     x += 1
    #     print('downloading: '+url,'\n')

if __name__=='__main__':
    html=gethtml('http://www.listeningexpress.com/studioclassroom/ad/')
    mp3list=getmp3url(html)
    downloadmp3s(mp3list)
    print('download success!')
