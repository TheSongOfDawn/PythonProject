# -*- coding: utf-8 -*-
import requests
import re
from  bs4 import BeautifulSoup

h = {'User-Agent':'"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0"'}
def getHTML(url):
    r=requests.get(url,headers=h)
    return r.content
def parseHTML(html):
    soup=BeautifulSoup(html,'html.parser')
    body=soup.body
    joke_allurl=soup.find_all(text=(u"瞎扯 · 如何正确地吐槽"))[0].parent.parent.parent['href']
    joke_url=url+joke_allurl[1:-1]+joke_allurl[-1]
    print joke_url
url = "http://daily.zhihu.com/"
html=getHTML(url)
parseHTML(html)
