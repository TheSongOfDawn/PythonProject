# -*- coding: utf-8 -*-
__author__ = 'lk'
import requests
import json
import time
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
s.post(url,data=Login,headers=head)
card_url = "http://web.cqust.edu.cn:9080/pnull.portal?.f=f1106&.pmn=view&action=informationCenterAjax&.ia=false&.pen=pe361"
card_result=s.get(card_url)
card_lis=card_result.json()
card_str= card_lis[0][u'description']
print card_str








