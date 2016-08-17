# -*- coding: utf-8 -*-
import requests
import json
import csv
from lxml import etree
from bs4 import BeautifulSoup
url='http://web.cqust.edu.cn:9080/userPasswordValidate.portal'
s=requests.session()
s.get(url)
cookie_value= ''
for x in s.cookies:
    if x.name == 'JSESSIONID':
        cookie_value = x.value
        break
head= {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':181,
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':cookie_value,
'Host':'web.cqust.edu.cn',
'Origin':'http://web.cqust.edu.cn',
'Referer':'http://web.cqust.edu.cn/',
'User-Agent':'Mozilla/5.0 (Winsdows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}
Login={'Login.Token1':'username',
	'Login.Token2':'password',
    'goto':'http://web.cqust.edu.cn:9080/loginSuccess.portal',
    'gotoOnFail':'http://web.cqust.edu.cn:9080/loginFailure.portal'}
a=s.post(url,data=Login,headers=head)
book_url = "http://libids.cqust.edu.cn/gethead.php"
book_result=s.get(book_url).content
soup=BeautifulSoup(book_result,'lxml')
table=soup.find('table',id='disp2').find_all('td')
i=-1
j=-1
for tr in table:
    i+=1
    if i<11:
	continue
    if i>60:
	break
    if i%10==2:
        if tr.string==None:
	    break
        print 'title:%s'%(tr.string)
    elif i%10==6:
	print 'Borrowing date:%s'%(tr.string)
    elif i%10==7:
        print 'Should date:%s'%(tr.string)
    else:
	continue
  


