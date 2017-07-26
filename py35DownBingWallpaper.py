# -*- coding: utf-8 -*-
__author__ = 'lk'
import requests
import re
import time
import os
import json
from bs4 import BeautifulSoup
def downpic(file_name,picurl):
# 判断是否存在D盘pic文件夹，不存在就新建，否则就不建立
    if os.path.exists(r'D:/pic/'):
        print ('pic文件夹已经在D盘存在，继续运行程序……')
    else:
        print ('pic文件夹不在D盘，新建文件夹')
        os.mkdir(r'D:/pic/')
    print ('文件夹建立成功，继续运行程序')
    pic = getHTML(picurl)
    fp = open('D:/pic/'+file_name, 'wb')
    fp.write(pic)
    fp.close()
def getHTML(url):
    r=requests.get(url)
    return r.content
url='http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
json_str_bytes=getHTML(url)#得到的是str
json_str=json_str_bytes.decode()
json_list=json.loads(json_str)#得到list
base_url="http://cn.bing.com/"
picurl=base_url+json_list['images'][0]['url']
print(picurl)
#这个是输入当前日期作为文件名
file_name=str(time.strftime('%Y-%m-%d',time.localtime(time.time())))+'.jpg'
downpic(file_name,picurl)
